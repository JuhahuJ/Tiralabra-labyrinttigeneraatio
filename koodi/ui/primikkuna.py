from ruudukko import Ruudukko
from random import choice, randrange
from tkinter import ttk, Canvas
import tkinter


class PrimIkkuna:
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

        apulista = []

        solu = ruudukko.ruudut[0][0]
        solu.oltujo = True
        apulista.append(solu.vas)
        apulista.append(solu.oik)
        apulista.append(solu.yl)
        apulista.append(solu.al)

        while len(apulista) > 0:
            valittuseina = choice(apulista)
            vastakkainenseina = ruudukko.vastakkainen_seina(valittuseina)
            if vastakkainenseina.y > -1 and vastakkainenseina.y < ruudukko.koko and vastakkainenseina.x > -1 and vastakkainenseina.x < ruudukko.koko:
                valittusolu = ruudukko.ruudut[ruudukko.vastakkainen_seina(
                    valittuseina).y][ruudukko.vastakkainen_seina(valittuseina).x]
                if valittusolu.oltujo is not solu.oltujo:
                    if valittuseina.suunta == "ylä":
                        apulista.append(valittusolu.vas)
                        apulista.append(valittusolu.oik)
                        apulista.append(valittusolu.yl)
                        valittusolu.oltujo = True
                        canvas.create_line(valittusolu.x*20+6, valittuseina.y*20+5,
                                           valittusolu.x*20+25, valittuseina.y*20+5, fill="white")
                    elif valittuseina.suunta == "ala":
                        apulista.append(valittusolu.vas)
                        apulista.append(valittusolu.oik)
                        apulista.append(valittusolu.al)
                        valittusolu.oltujo = True
                        canvas.create_line(valittusolu.x*20+6, valittusolu.y*20+5,
                                           valittusolu.x*20+25, valittusolu.y*20+5, fill="white")
                    elif valittuseina.suunta == "vasen":
                        apulista.append(valittusolu.vas)
                        apulista.append(valittusolu.al)
                        apulista.append(valittusolu.yl)
                        valittusolu.oltujo = True
                        canvas.create_line(valittuseina.x*20+5, valittusolu.y*20+6,
                                           valittuseina.x*20+5, valittusolu.y*20+25, fill="white")
                    elif valittuseina.suunta == "oikea":
                        apulista.append(valittusolu.al)
                        apulista.append(valittusolu.oik)
                        apulista.append(valittusolu.yl)
                        valittusolu.oltujo = True
                        canvas.create_line(valittusolu.x*20+5, valittusolu.y*20+6,
                                           valittusolu.x*20+5, valittusolu.y*20+25, fill="white")
                    solu = valittusolu
            apulista.remove(valittuseina)

        button = ttk.Button(
            master=self._frame,
            text="Mene takaisin alkuun",
            command=self._aloitus_kasittely
        ).pack()
        button2 = ttk.Button(
            master=self._frame,
            text="Luo uusi labyrintti",
            command=lambda: self._avaa_uudelleen_prim(self.koko)
        ).pack()
