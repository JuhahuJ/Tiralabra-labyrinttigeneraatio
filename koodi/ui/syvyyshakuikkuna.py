from solu import Solu
from ruudukko import Ruudukko
from random import randrange
from tkinter import ttk, Canvas
import tkinter

class SyvyyshakuIkkuna:
    def __init__(self, root, aloitus_kasittely, avaa_uudelleen, koko):
        self._root = root
        self._frame = None
        self._aloitus_kasittely = aloitus_kasittely
        self._avaa_uudelleen = avaa_uudelleen
        self.koko = int(koko)
        self._initialize()

    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        canvas = Canvas(self._frame, width = self.koko*20+10, height =self.koko*20+10, bg="white")
        canvas.pack()

        ruutus = Ruudukko(self.koko)
        ruutus.luo()
        paikka = 0

        for i in range(self.koko+1):
            canvas.create_line(paikka*20+5, 5, paikka*20+5, 20*self.koko+5)
            paikka += 1
        paikka = 0
        for j in range(self.koko+1):
            canvas.create_line(5, paikka*20+5, 20*self.koko+5, paikka*20+5)
            paikka += 1
        

        tamanhetkinensolu = None
        lista = []

        aloitusruutu = ruutus.ruudut[randrange(self.koko)][randrange(self.koko)]
        aloitusruutu.oltujo = True
        lista.append(aloitusruutu)
        apu = 0
        while len(lista) > 0:
            viereiset = []
            nykyinensolu = lista[-1]
            lista.pop()
            if nykyinensolu.y == 0:
                pass
            elif ruutus.ruudut[nykyinensolu.y-1][nykyinensolu.x].oltujo == False:
                viereiset.append(ruutus.ruudut[nykyinensolu.y-1][nykyinensolu.x])
            if nykyinensolu.y == self.koko-1:
                pass
            elif ruutus.ruudut[nykyinensolu.y+1][nykyinensolu.x].oltujo == False:
                viereiset.append(ruutus.ruudut[nykyinensolu.y+1][nykyinensolu.x])
            if nykyinensolu.x == 0:
                pass
            elif ruutus.ruudut[nykyinensolu.y][nykyinensolu.x-1].oltujo == False:
                viereiset.append(ruutus.ruudut[nykyinensolu.y][nykyinensolu.x-1])
            if nykyinensolu.x == self.koko-1:
                pass
            elif ruutus.ruudut[nykyinensolu.y][nykyinensolu.x+1].oltujo == False:
                viereiset.append(ruutus.ruudut[nykyinensolu.y][nykyinensolu.x+1])
            if len(viereiset) > 0:
                lista.append(nykyinensolu)
                seuraavasolu = viereiset[randrange(len(viereiset))]
                seuraavasolu.oltujo = True
                lista.append(seuraavasolu)
                if seuraavasolu.x > nykyinensolu.x:
                    canvas.create_line(seuraavasolu.x*20+5, nykyinensolu.y*20+6, seuraavasolu.x*20+5, seuraavasolu.y*20+25, fill="white")
                if seuraavasolu.x < nykyinensolu.x:
                    canvas.create_line(nykyinensolu.x*20+5, nykyinensolu.y*20+6, nykyinensolu.x*20+5, seuraavasolu.y*20+25, fill="white")
                if seuraavasolu.y > nykyinensolu.y:
                    canvas.create_line(nykyinensolu.x*20+6, seuraavasolu.y*20+5, seuraavasolu.x*20+25, seuraavasolu.y*20+5, fill="white")
                if seuraavasolu.y < nykyinensolu.y:
                    canvas.create_line(nykyinensolu.x*20+6, nykyinensolu.y*20+5, seuraavasolu.x*20+25, nykyinensolu.y*20+5, fill="white")

        button = ttk.Button(
            master=self._frame,
            text="Mene takaisin alkuun",
            command=self._aloitus_kasittely
        ).pack()
        button2 = ttk.Button(
            master=self._frame,
            text="Luo uusi labyrintti",
            command=lambda: self._avaa_uudelleen(self.koko)
        ).pack()
        