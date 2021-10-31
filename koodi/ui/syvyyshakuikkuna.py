from solu import Solu
from ruudukko import Ruudukko
from random import randrange
from tkinter import ttk, Canvas
import tkinter
from time import sleep


class SyvyyshakuIkkuna:
    def __init__(self, root, aloitus_kasittely, avaa_uudelleen_syvyys, koko):
        self._root = root
        self._frame = None
        self._aloitus_kasittely = aloitus_kasittely
        self._avaa_uudelleen_syvyys = avaa_uudelleen_syvyys
        self.koko = int(koko)
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def nayta_miten_luotu(self, canvas, lapikaynti, nopeus):
        paikka = 0
        for i in range(self.koko+1):
            canvas.create_line(paikka*20+5, 5, paikka*20+5, 20*self.koko+5)
            paikka += 1
        paikka = 0
        for j in range(self.koko+1):
            canvas.create_line(5, paikka*20+5, 20*self.koko+5, paikka*20+5)
            paikka += 1
        canvas.create_rectangle(lapikaynti[0].x*20+7, lapikaynti[0].y*20+7,
                                lapikaynti[0].x*20+23, lapikaynti[0].y*20+23, fill="green")
        for solu in range(len(lapikaynti)):
            if solu != len(lapikaynti)-1:
                if lapikaynti[solu+1].x > lapikaynti[solu].x:
                    canvas.create_line(lapikaynti[solu+1].x*20+5, lapikaynti[solu].y*20+6,
                                       lapikaynti[solu+1].x*20+5, lapikaynti[solu+1].y*20+25, fill="white")
                if lapikaynti[solu+1].x < lapikaynti[solu].x:
                    canvas.create_line(lapikaynti[solu].x*20+5, lapikaynti[solu].y*20+6,
                                       lapikaynti[solu].x*20+5, lapikaynti[solu+1].y*20+25, fill="white")
                if lapikaynti[solu+1].y > lapikaynti[solu].y:
                    canvas.create_line(lapikaynti[solu].x*20+6, lapikaynti[solu+1].y*20+5,
                                       lapikaynti[solu+1].x*20+25, lapikaynti[solu+1].y*20+5, fill="white")
                if lapikaynti[solu+1].y < lapikaynti[solu].y:
                    canvas.create_line(lapikaynti[solu].x*20+6, lapikaynti[solu].y*20+5,
                                       lapikaynti[solu+1].x*20+25, lapikaynti[solu].y*20+5, fill="white")
                canvas.create_rectangle(lapikaynti[solu+1].x*20+12, lapikaynti[solu+1].y*20+12,
                                        lapikaynti[solu+1].x*20+18, lapikaynti[solu+1].y*20+18, fill="blue", outline="")
                canvas.create_rectangle(lapikaynti[solu].x*20+10, lapikaynti[solu].y*20+10,
                                        lapikaynti[solu].x*20+20, lapikaynti[solu].y*20+20, fill="white", outline="")
                self._root.update()
                sleep(nopeus)

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        canvas = Canvas(self._frame, width=self.koko*20+10,
                        height=self.koko*20+10, bg="white")
        canvas.pack()

        ruutus = Ruudukko(self.koko)
        paikka = 0

        for i in range(self.koko+1):
            canvas.create_line(paikka*20+5, 5, paikka*20+5, 20*self.koko+5)
            paikka += 1
        paikka = 0
        for j in range(self.koko+1):
            canvas.create_line(5, paikka*20+5, 20*self.koko+5, paikka*20+5)
            paikka += 1

        lista = []
        lapikaynti = []

        aloitusruutu = ruutus.ruudut[randrange(
            self.koko)][randrange(self.koko)]
        aloitusruutu.oltujo = True
        lista.append(aloitusruutu)
        while len(lista) > 0:
            viereiset = []
            nykyinensolu = lista[-1]
            lapikaynti.append(nykyinensolu)
            lista.pop()
            if nykyinensolu.y == 0:
                pass
            elif ruutus.ruudut[nykyinensolu.y-1][nykyinensolu.x].oltujo == False:
                viereiset.append(
                    ruutus.ruudut[nykyinensolu.y-1][nykyinensolu.x])
            if nykyinensolu.y == self.koko-1:
                pass
            elif ruutus.ruudut[nykyinensolu.y+1][nykyinensolu.x].oltujo == False:
                viereiset.append(
                    ruutus.ruudut[nykyinensolu.y+1][nykyinensolu.x])
            if nykyinensolu.x == 0:
                pass
            elif ruutus.ruudut[nykyinensolu.y][nykyinensolu.x-1].oltujo == False:
                viereiset.append(
                    ruutus.ruudut[nykyinensolu.y][nykyinensolu.x-1])
            if nykyinensolu.x == self.koko-1:
                pass
            elif ruutus.ruudut[nykyinensolu.y][nykyinensolu.x+1].oltujo == False:
                viereiset.append(
                    ruutus.ruudut[nykyinensolu.y][nykyinensolu.x+1])
            if len(viereiset) > 0:
                lista.append(nykyinensolu)
                seuraavasolu = viereiset[randrange(len(viereiset))]
                seuraavasolu.oltujo = True
                lista.append(seuraavasolu)
                if seuraavasolu.x > nykyinensolu.x:
                    canvas.create_line(seuraavasolu.x*20+5, nykyinensolu.y*20+6,
                                       seuraavasolu.x*20+5, seuraavasolu.y*20+25, fill="white")
                if seuraavasolu.x < nykyinensolu.x:
                    canvas.create_line(nykyinensolu.x*20+5, nykyinensolu.y*20+6,
                                       nykyinensolu.x*20+5, seuraavasolu.y*20+25, fill="white")
                if seuraavasolu.y > nykyinensolu.y:
                    canvas.create_line(nykyinensolu.x*20+6, seuraavasolu.y*20+5,
                                       seuraavasolu.x*20+25, seuraavasolu.y*20+5, fill="white")
                if seuraavasolu.y < nykyinensolu.y:
                    canvas.create_line(nykyinensolu.x*20+6, nykyinensolu.y*20+5,
                                       seuraavasolu.x*20+25, nykyinensolu.y*20+5, fill="white")

        nopeus = tkinter.StringVar(self._frame)
        nopeus.set("0.07")

        val_lista = [0.01, 0.07, 0.15, 0.5, 1]

        button = ttk.Button(
            master=self._frame,
            text="Mene takaisin alkuun",
            command=self._aloitus_kasittely
        ).pack()
        button2 = ttk.Button(
            master=self._frame,
            text="Luo uusi labyrintti",
            command=lambda: self._avaa_uudelleen_syvyys(self.koko)
        ).pack()
        button3 = ttk.Button(
            master=self._frame,
            text="Näytä labyrintin luominen nopeudella",
            command=lambda: self.nayta_miten_luotu(
                canvas, lapikaynti, float(nopeus.get()))
        ).pack(side="left")
        nopeus_valinta = tkinter.OptionMenu(
            self._frame, nopeus, *val_lista).pack(side="right")
