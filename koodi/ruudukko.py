from solu import Solu
from copy import copy


class Ruudukko:
    '''Ruudukko olio, jolle annetaan koko.'''

    def __init__(self, koko: int, ruudut=[]):
        self.koko = koko
        self.ruudut = ruudut

    def luo(self):
        '''Täyttää ruudut soluilla perustuen annettuun kokoon, jolloin ruudukossa on koko*koko solua.

        Ensimmäiseksi tyhjentää ruudut.

        Silmukassa: Lisää ruutuihin väliaikaisen arvon, joka korvataan myöhemmin ja luo tyhjän apulistan.

        Sisemmässä silmukassa: Luo solun koordinaateilla i, j, missä i on y ja j on x ja koordinaatit kasvavat ylhäältä alas, vasemmalta oikealle,
        lisää solun apulistaan.

        Ylemmässä silmukassa: korvaa väliaikaisen arvon apulistalla.
        '''

        self.ruudut = []
        for i in range(self.koko):
            self.ruudut.append("väliaikainen arvo")
            apulista = []
            for j in range(self.koko):
                solu = Solu(i, j)
                solu.luo_seinat()
                apulista.append(solu)
            self.ruudut[i] = apulista

    def vastakkainen_seina(self, seina):
        if seina.suunta == "ylä":
            viereiset = copy(seina)
            viereiset.y -= 1
            return viereiset
        elif seina.suunta == "ala":
            viereiset = copy(seina)
            viereiset.y += 1
            return viereiset
        elif seina.suunta == "vasen":
            viereiset = copy(seina)
            viereiset.x -= 1
            return viereiset
        elif seina.suunta == "oikea":
            viereiset = copy(seina)
            viereiset.x += 1
            return viereiset