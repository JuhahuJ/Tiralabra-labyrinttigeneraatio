from tkinter import ttk, Canvas
import tkinter
from time import sleep
from labyrintit.binaaripuu import Binaaripuu


class BinaaripuuIkkuna:
    """Luokka, joka vastaa labyrintin luomisesta ja esittämisestä binääripuualgoritmilla."""

    def __init__(self, root, aloitus_kasittely, avaa_uudelleen_binaaripuu, koko):
        self._root = root
        self._frame = None
        self._aloitus_kasittely = aloitus_kasittely
        self._avaa_uudelleen_binaaripuu = avaa_uudelleen_binaaripuu
        self.koko = int(koko)
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def nayta_miten_luotu(self, canvas, lapikaynti, nopeus):
        """Näyttää, miten labyrintti luotiin.
        Args:
            canvas: Tkinterin canvas, jolle labyrintti piirretään.
            lapikaynti: Lista, joka koostuu soluista ja suunnista, joista solujen välinen seinä poistetaan.
            nopeus: Luku, joka kertoo kuinka nopeasti labyrintin luomista käydään läpi.
        """

        for i in range(self.koko+1):
            canvas.create_line(i*20+5, 5, i*20+5, 20*self.koko+5)
        for j in range(self.koko+1):
            canvas.create_line(5, j*20+5, 20*self.koko+5, j*20+5)

        for solu in lapikaynti:
            if solu[1] == "alas" and solu[0].y < self.koko-1:
                canvas.create_line(solu[0].x*20+6, solu[0].y*20+25,
                                   solu[0].x*20+25, solu[0].y*20+25, fill="white")
            elif solu[1] == "alas" and solu[0].x < self.koko-1:
                canvas.create_line(solu[0].x*20+25, solu[0].y*20+6,
                                   solu[0].x*20+25, solu[0].y*20+25, fill="white")
            elif solu[1] == "oikealle" and solu[0].x < self.koko-1:
                canvas.create_line(solu[0].x*20+25, solu[0].y*20+6,
                                   solu[0].x*20+25, solu[0].y*20+25, fill="white")
            elif solu[1] == "oikealle" and solu[0].y < self.koko-1:
                canvas.create_line(solu[0].x*20+6, solu[0].y*20+25,
                                   solu[0].x*20+25, solu[0].y*20+25, fill="white")

            canvas.create_rectangle(
                solu[0].x*20+12, solu[0].y*20+12, solu[0].x*20+18, solu[0].y*20+18, fill="blue")
            self._root.update()
            sleep(nopeus)
            canvas.create_rectangle(
                solu[0].x*20+10, solu[0].y*20+10, solu[0].x*20+20, solu[0].y*20+20, fill="white", outline="")

    def _initialize(self):
        """Luo labyrintin ja napit.

        Aluksi luo ruudukko olion ja piirtää aloitusikkunassa annetun koon perusteella ruudukon.
        Sitten käy ruudukon läpi solu kerrallaan valiten joka solulle poistetaanko seinä sen alapuolelta vai oikealta.
        """

        self._frame = ttk.Frame(master=self._root)
        canvas = Canvas(self._frame, width=self.koko*20+10,
                        height=self.koko*20+10, bg="white")
        canvas.pack()

        for i in range(self.koko+1):
            canvas.create_line(i*20+5, 5, i*20+5, 20*self.koko+5)
        for j in range(self.koko+1):
            canvas.create_line(5, j*20+5, 20*self.koko+5, j*20+5)

        lapikaynti = Binaaripuu(self.koko).luo_labyrintti()

        for solu in lapikaynti:
            if solu[1] == "alas" and solu[0].y < self.koko-1:
                canvas.create_line(solu[0].x*20+6, solu[0].y*20+25,
                                   solu[0].x*20+25, solu[0].y*20+25, fill="white")
            elif solu[1] == "alas" and solu[0].x < self.koko-1:
                canvas.create_line(solu[0].x*20+25, solu[0].y*20+6,
                                   solu[0].x*20+25, solu[0].y*20+25, fill="white")
            elif solu[1] == "oikealle" and solu[0].x < self.koko-1:
                canvas.create_line(solu[0].x*20+25, solu[0].y*20+6,
                                   solu[0].x*20+25, solu[0].y*20+25, fill="white")
            elif solu[1] == "oikealle" and solu[0].y < self.koko-1:
                canvas.create_line(solu[0].x*20+6, solu[0].y*20+25,
                                   solu[0].x*20+25, solu[0].y*20+25, fill="white")

        nopeus = tkinter.StringVar(self._frame)
        nopeus.set("0.07")

        val_lista = [0.001, 0.01, 0.07, 0.15, 0.5, 1]

        takaisin_alkuuna_nappi = ttk.Button(
            master=self._frame,
            text="Mene takaisin alkuun",
            command=self._aloitus_kasittely)

        luo_uusi_labyrintti_nappi = ttk.Button(
            master=self._frame,
            text="Luo uusi labyrintti",
            command=lambda: self._avaa_uudelleen_binaaripuu(self.koko))

        nayta_labyrintin_luominen_nappi = ttk.Button(
            master=self._frame,
            text="Näytä labyrintin luominen nopeudella",
            command=lambda: self.nayta_miten_luotu(
                canvas, lapikaynti, float(nopeus.get())))

        nopeus_valinta = tkinter.OptionMenu(self._frame, nopeus, *val_lista)
        takaisin_alkuuna_nappi.pack()
        luo_uusi_labyrintti_nappi.pack()
        nayta_labyrintin_luominen_nappi.pack(side="left")
        nopeus_valinta.pack(side="right")
