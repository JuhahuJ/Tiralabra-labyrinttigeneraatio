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
        paikka = 0

        for i in range(self.koko+1):
            canvas.create_line(paikka*20+5, 5, paikka*20+5, 20*self.koko+5)
            paikka += 1
        paikka = 0
        for j in range(self.koko+1):
            canvas.create_line(5, paikka*20+5, 20*self.koko+5, paikka*20+5)
            paikka += 1
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
            canvas.create_rectangle(solu[0].x*20+12, solu[0].y*20+12, solu[0].x*20+18, solu[0].y*20+18,fill="blue")
            self._root.update()
            sleep(0.1)
            canvas.create_rectangle(solu[0].x*20+10, solu[0].y*20+10, solu[0].x*20+20, solu[0].y*20+20,fill="white", outline="")

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        canvas = Canvas(self._frame, width=self.koko*20+10,
                        height=self.koko*20+10, bg="white")
        canvas.pack()

        ruudukko = Ruudukko(self.koko)

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
                suunta = choice(["alas","oikealle"])
                lapikaynti.append([solu,suunta])
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
