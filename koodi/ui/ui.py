from ui.aloitusikkuna import AloitusIkkuna
from ui.syvyyshakuikkuna import SyvyyshakuIkkuna
from ui.primikkuna import PrimIkkuna
from ui.binaaripuuikkuna import BinaaripuuIkkuna


class UI:
    def __init__(self, root):
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
        self._nykyinen_ikkuna = AloitusIkkuna(
            self._root, self._syvyyshaku_kasittely, self._prim_kasittely, self._binaaripuu_kasittely,)
        self._nykyinen_ikkuna.pack()

    def _syvyyshaku_kasittely(self, koko):
        self._avaa_syvyyshaku_ikkuna(koko)

    def _aloitus_kasittely(self):
        self._avaa_aloitus_ikkuna()

    def _avaa_syvyyshaku_ikkuna(self, koko):
        self._piilota_nykyinen_ikkuna()
        self._nykyinen_ikkuna = SyvyyshakuIkkuna(
            self._root, self._aloitus_kasittely, self._avaa_uudelleen_syvyys, koko)
        self._nykyinen_ikkuna.pack()

    def _avaa_uudelleen_syvyys(self, koko):
        self._avaa_syvyyshaku_ikkuna(koko)

    def _avaa_uudelleen_prim(self, koko):
        self._avaa_prim_ikkuna(koko)

    def _avaa_prim_ikkuna(self, koko):
        self._piilota_nykyinen_ikkuna()
        self._nykyinen_ikkuna = PrimIkkuna(
            self._root, self._aloitus_kasittely, self._avaa_uudelleen_prim, koko)
        self._nykyinen_ikkuna.pack()

    def _prim_kasittely(self, koko):
        self._avaa_prim_ikkuna(koko)

    def _avaa_uudelleen_binaaripuu(self, koko):
        self._avaa_binaaripuu_ikkuna(koko)

    def _avaa_binaaripuu_ikkuna(self, koko):
        self._piilota_nykyinen_ikkuna()
        self._nykyinen_ikkuna = BinaaripuuIkkuna(
            self._root, self._aloitus_kasittely, self._avaa_uudelleen_binaaripuu, koko)
        self._nykyinen_ikkuna.pack()

    def _binaaripuu_kasittely(self, koko):
        self._avaa_binaaripuu_ikkuna(koko)
