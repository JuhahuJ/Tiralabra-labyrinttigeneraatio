from random import choice, randrange
from tkinter import ttk, Canvas
import tkinter
from time import sleep
from labyrintit.prim import Prim


class PrimIkkuna:
    """Luokka, joka vastaa labyrintin luomisesta ja esittämisestä primin algoritmilla."""

    def __init__(self, root, aloitus_kasittely, avaa_uudelleen_prim, koko):
        self._root = root
        self._frame = None
        self._aloitus_kasittely = aloitus_kasittely
        self._avaa_uudelleen_prim = avaa_uudelleen_prim
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

        for k in lapikaynti:
            if k[1] == "ala":
                canvas.create_line(k[0].x*20+6, k[0].y*20+5,
                                   k[0].x*20+25, k[0].y*20+5, fill="white")
            if k[1] == "ylä":
                canvas.create_line(k[0].x*20+6, (k[0].y+1)*20+5,
                                   k[0].x*20+25, (k[0].y+1)*20+5, fill="white")
            if k[1] == "vasen":
                canvas.create_line((k[0].x+1)*20+5, k[0].y*20+6,
                                   (k[0].x+1)*20+5, k[0].y*20+25, fill="white")
            if k[1] == "oikea":
                canvas.create_line(k[0].x*20+5, k[0].y*20+6,
                                   k[0].x*20+5, k[0].y*20+25, fill="white")
            self._root.update()
            sleep(nopeus)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        canvas = Canvas(self._frame, width=self.koko*20+10,
                        height=self.koko*20+10, bg="white")
        canvas.pack()

        for i in range(self.koko+1):
            canvas.create_line(i*20+5, 5, i*20+5, 20*self.koko+5)
        for j in range(self.koko+1):
            canvas.create_line(5, j*20+5, 20*self.koko+5, j*20+5)

        lapikaynti = Prim(self.koko).luo_labyrintti()

        for k in lapikaynti:
            if k[1] == "ala":
                canvas.create_line(k[0].x*20+6, k[0].y*20+5,
                                   k[0].x*20+25, k[0].y*20+5, fill="white")
            if k[1] == "ylä":
                canvas.create_line(k[0].x*20+6, (k[0].y+1)*20+5,
                                   k[0].x*20+25, (k[0].y+1)*20+5, fill="white")
            if k[1] == "vasen":
                canvas.create_line((k[0].x+1)*20+5, k[0].y*20+6,
                                   (k[0].x+1)*20+5, k[0].y*20+25, fill="white")
            if k[1] == "oikea":
                canvas.create_line(k[0].x*20+5, k[0].y*20+6,
                                   k[0].x*20+5, k[0].y*20+25, fill="white")

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
            command=lambda: self._avaa_uudelleen_prim(self.koko))

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
