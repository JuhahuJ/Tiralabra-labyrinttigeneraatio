from copy import copy
from solu import Solu


class Ruudukko:
    '''Ruudukko olio, jolle annetaan koko.'''

    def __init__(self, koko: int, ruudut=[]):
        self.koko = koko
        self.ruudut = ruudut
        self.luo()

    def luo(self):
        self.ruudut = []

        for i in range(self.koko):
            self.ruudut.append("väliaikainen arvo")
            apulista = []

            for j in range(self.koko):
                solu = Solu(i, j)
                solu.luo_seinat()
                apulista.append(solu)

            self.ruudut[i] = apulista

    def viereiset_solut(self, solu_y, solu_x):
        viereiset = []

        if solu_y > 0 and self.ruudut[solu_y-1][solu_x].oltujo is False:
            viereiset.append(self.ruudut[solu_y-1][solu_x])

        if solu_y < len(self.ruudut)-1 and self.ruudut[solu_y+1][solu_x].oltujo is False:
            viereiset.append(self.ruudut[solu_y+1][solu_x])

        if solu_x > 0 and self.ruudut[solu_y][solu_x-1].oltujo is False:
            viereiset.append(self.ruudut[solu_y][solu_x-1])

        if solu_x < len(self.ruudut)-1 and self.ruudut[solu_y][solu_x+1].oltujo is False:
            viereiset.append(self.ruudut[solu_y][solu_x+1])

        return viereiset

    def vastakkainen_seina(self, seina):
        vastakkainen_seina = copy(seina)
        if seina.suunta == "ylä":
            vastakkainen_seina.y -= 1
            return vastakkainen_seina

        if seina.suunta == "ala":
            vastakkainen_seina.y += 1
            return vastakkainen_seina

        if seina.suunta == "vasen":
            vastakkainen_seina.x -= 1
            return vastakkainen_seina

        if seina.suunta == "oikea":
            vastakkainen_seina.x += 1
            return vastakkainen_seina
