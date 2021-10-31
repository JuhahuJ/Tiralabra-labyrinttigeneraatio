from random import choice
from ruudukko import Ruudukko


class Binaaripuu:
    def __init__(self, koko):
        self.koko = koko

    def luo_labyrintti(self):
        ruudukko = Ruudukko(self.koko)
        lapikaynti = []

        for i in range(len(ruudukko.ruudut)):
            for solu in ruudukko.ruudut[i]:
                suunta = choice(["alas", "oikealle"])
                lapikaynti.append([solu, suunta])

        return lapikaynti
