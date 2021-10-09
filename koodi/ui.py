from tkinter import Tk
from aloitusikkuna import AloitusIkkuna
from syvyyshakuikkuna import SyvyyshakuIkkuna

class UI:
    def __init__(self,root):
        self._root = root
        self._nykyinen_ikkuna = None

    def alku(self):
        self._avaa_aloitus_ikkuna()
    
    def _piilota_nykyinen_ikkuna(self):
        if self._nykyinen_ikkuna:
            self._nykyinen_ikkuna.destroy()
        self._nykyinen_ikkuna = None

    def _avaa_aloitus_ikkuna(self):
        self._piilota_nykyinen_ikkuna()
        self._nykyinen_ikkuna = AloitusIkkuna(self._root, self._syvyyshaku_kasittely)
        self._nykyinen_ikkuna.pack()

    def _syvyyshaku_kasittely(self, koko):
        self._avaa_syvyyshaku_ikkuna(koko)
    
    def _aloitus_kasittely(self):
        self._avaa_aloitus_ikkuna()

    def _avaa_syvyyshaku_ikkuna(self, koko):
        self._piilota_nykyinen_ikkuna()
        self._nykyinen_ikkuna = SyvyyshakuIkkuna(self._root, self._aloitus_kasittely, self._avaa_uudelleen, koko)
        self._nykyinen_ikkuna.pack()

    def _avaa_uudelleen(self, koko):
        self._avaa_syvyyshaku_ikkuna(koko)

ikkuna = Tk()

ui = UI(ikkuna)
ui.alku()

ikkuna.mainloop()