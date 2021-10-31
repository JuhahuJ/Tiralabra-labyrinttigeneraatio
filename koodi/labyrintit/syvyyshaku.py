from random import randrange, choice
from ruudukko import Ruudukko

class Syvyyshaku:
    def __init__(self, koko):
        self.koko = koko

    def luo_labyrintti(self):
        ruudukko = Ruudukko(self.koko)
        lapikaynti = []
        aloitusruutu = ruudukko.ruudut[randrange(self.koko)][randrange(self.koko)]
        aloitusruutu.oltujo = True
        solulista = [aloitusruutu]

        while len(solulista) > 0:
            nykyinensolu = solulista[-1]
            viereiset = ruudukko.viereiset_solut(nykyinensolu.y, nykyinensolu.x)
            lapikaynti.append(nykyinensolu)
            solulista.pop()

            if len(viereiset) > 0:
                solulista.append(nykyinensolu)
                seuraavasolu = choice(viereiset)
                seuraavasolu.oltujo = True
                solulista.append(seuraavasolu)

        return lapikaynti