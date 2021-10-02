from solu import solu
import tkinter

class ruudukko:
    def __init__(self,koko:int,root,ruudut=[]):
        self.koko = koko
        self.ruudut = ruudut
        self.root = root

    def luo(self):
        for i in range(self.koko):
            apulista = []
            for j in range(self.koko):
                solus = solu(i,j)
                apulista.append(solus)
                tkinter.Label(self.root, text='y%s/x%s'%(j,i) ).grid(row=j,column=i)
            self.ruudut.append(apulista)
