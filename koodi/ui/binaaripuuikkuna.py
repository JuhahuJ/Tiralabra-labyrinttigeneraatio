from ruudukko import Ruudukko
from random import choice
from tkinter import ttk, Canvas
import tkinter
from time import sleep



class BinaaripuuIkkuna:
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

    def nayta_miten_luotu(self, canvas, lapikaynti):
        canvas.create_rectangle(lapikaynti[0].x*20+7, lapikaynti[0].y*20+7, lapikaynti[0].x*20+23, lapikaynti[0].y*20+23,fill="green")
        for solu in range(len(lapikaynti)):
            canvas.create_rectangle(lapikaynti[solu].x*20+12, lapikaynti[solu].y*20+12, lapikaynti[solu].x*20+18, lapikaynti[solu].y*20+18,fill="blue")
            canvas.create_rectangle(lapikaynti[solu-1].x*20+10, lapikaynti[solu-1].y*20+10, lapikaynti[solu-1].x*20+20, lapikaynti[solu-1].y*20+20,fill="red")
            self._root.update()
            sleep(0.1)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        canvas = Canvas(self._frame, width=self.koko*20+10,
                        height=self.koko*20+10, bg="white")
        canvas.pack()

        ruudukko = Ruudukko(self.koko)
        ruudukko.luo()

        paikka = 0

        for i in range(self.koko+1):
            canvas.create_line(paikka*20+5, 5, paikka*20+5, 20*self.koko+5)
            paikka += 1
        paikka = 0
        for j in range(self.koko+1):
            canvas.create_line(5, paikka*20+5, 20*self.koko+5, paikka*20+5)
            paikka += 1

        lapikaynti = []

        for i in range(len(ruudukko.ruudut)):
            for solu in ruudukko.ruudut[i]:
                lapikaynti.append(solu)
                suunta = choice(["alas","oikealle"])
                if suunta == "alas" and solu.y < self.koko-1:
                    canvas.create_line(solu.x*20+6, solu.y*20+25,
                                           solu.x*20+25, solu.y*20+25, fill="white")
                elif suunta == "alas" and solu.x < self.koko-1:
                    canvas.create_line(solu.x*20+25, solu.y*20+6,
                                           solu.x*20+25, solu.y*20+25, fill="white")
                elif suunta == "oikealle" and solu.x < self.koko-1:
                    canvas.create_line(solu.x*20+25, solu.y*20+6,
                                           solu.x*20+25, solu.y*20+25, fill="white")
                elif suunta == "oikealle" and solu.y < self.koko-1:
                    canvas.create_line(solu.x*20+6, solu.y*20+25,
                                           solu.x*20+25, solu.y*20+25, fill="white")

        

        button = ttk.Button(
            master=self._frame,
            text="Mene takaisin alkuun",
            command=self._aloitus_kasittely
        ).pack()
        button2 = ttk.Button(
            master=self._frame,
            text="Luo uusi labyrintti",
            command=lambda: self._avaa_uudelleen_binaaripuu(self.koko)
        ).pack()
        button3 = ttk.Button(
            master=self._frame,
            text="Näytä labyrintin luominen",
            command=lambda: self.nayta_miten_luotu(canvas, lapikaynti)
        ).pack()
