from solu import solu
from ruudukko import ruudukko
from random import randrange
from tkinter import *
import tkinter
from PIL import Image, ImageTk

root = Tk()
koko = 9
canvas = Canvas(root, width = koko*20+10, height =koko*20+10, bg="white")
canvas.pack()

ruutus = ruudukko(koko)
ruutus.luo()
paikka = 0

for i in range(koko+1):
    canvas.create_line(paikka*20+5, 5, paikka*20+5, 20*koko+5)
    paikka += 1
paikka = 0
for j in range(koko+1):
    canvas.create_line(5, paikka*20+5, 20*koko+5, paikka*20+5)
    paikka += 1

tamanhetkinensolu = None
lista = []

aloitusruutu = ruutus.ruudut[randrange(koko)][randrange(koko)]
aloitusruutu.oltujo = True
lista.append(aloitusruutu)
while len(lista) > 0:
    viereiset = []
    nykyinensolu = lista[-1]
    lista.pop()
    if nykyinensolu.y == 0:
        pass
    elif ruutus.ruudut[nykyinensolu.y-1][nykyinensolu.x].oltujo == False:
        viereiset.append(ruutus.ruudut[nykyinensolu.y-1][nykyinensolu.x])
    if nykyinensolu.y == koko-1:
        pass
    elif ruutus.ruudut[nykyinensolu.y+1][nykyinensolu.x].oltujo == False:
        viereiset.append(ruutus.ruudut[nykyinensolu.y+1][nykyinensolu.x])
    if nykyinensolu.x == 0:
        pass
    elif ruutus.ruudut[nykyinensolu.y][nykyinensolu.x-1].oltujo == False:
        viereiset.append(ruutus.ruudut[nykyinensolu.y][nykyinensolu.x-1])
    if nykyinensolu.x == koko-1:
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

root.mainloop()