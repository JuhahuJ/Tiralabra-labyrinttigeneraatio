from solu import solu
from ruudukko import ruudukko
from random import randrange
from tkinter import Tk, ttk
import tkinter

root = Tk()
root.title("TkInter example")
koko = 5
ruutus = ruudukko(koko,root)
ruutus.luo()

tamanhetkinensolu = None
lista = []

aloitusruutu = ruutus.ruudut[0][0]
aloitusruutu.oltujo = True
lista.append(aloitusruutu)
while len(lista) > 0:
    viereiset = []
    nykyinensolu = lista[-1]
    tkinter.Label(root, text="käyty", borderwidth=1 ).grid(row=nykyinensolu.y,column=nykyinensolu.x)
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
    root.update()

root.mainloop()