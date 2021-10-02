from solu import solu
from ruudukko import ruudukko
from random import randrange
from tkinter import *
import tkinter
from PIL import Image, ImageTk

root = Tk()
koko = 5
ruutus = ruudukko(koko,root)
ruutus.luo()

photo = tkinter.PhotoImage(file="y.png")
photo2 = tkinter.PhotoImage(file="v.png")

tamanhetkinensolu = None
lista = []

aloitusruutu = ruutus.ruudut[0][0]
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
        print(seuraavasolu.koordinaatit())

kuva = tkinter.Label(root, image=photo)
kuva.grid(row=0,column=0)
kuva2 = tkinter.Label(root, image=photo2)
kuva2.grid(row=0,column=1)


root.mainloop()