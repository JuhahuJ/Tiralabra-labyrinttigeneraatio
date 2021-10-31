from random import randrange, choice
from ruudukko import Ruudukko

class Prim:
    def __init__(self, koko):
        self.koko = koko

    def luo_labyrintti(self):
        ruudukko = Ruudukko(self.koko)
        solu = ruudukko.ruudut[randrange(self.koko)][randrange(self.koko)]
        solu.oltujo = True
        seinalista = [solu.vas, solu.oik, solu.yl, solu.al]
        lapikaynti = []

        while len(seinalista) > 0:
            valittuseina = choice(seinalista)
            vastakkainenseina = ruudukko.vastakkainen_seina(valittuseina)

            if vastakkainenseina.y > -1 and vastakkainenseina.y < ruudukko.koko and vastakkainenseina.x > -1 and vastakkainenseina.x < ruudukko.koko:
                valittusolu = ruudukko.ruudut[ruudukko.vastakkainen_seina(
                    valittuseina).y][ruudukko.vastakkainen_seina(valittuseina).x]

                if valittusolu.oltujo is not solu.oltujo:
                    if valittuseina.suunta == "ylä":
                        seinalista.append(valittusolu.vas)
                        seinalista.append(valittusolu.oik)
                        seinalista.append(valittusolu.yl)
                        valittusolu.oltujo = True

                        lapikaynti.append([valittusolu, valittuseina.suunta])

                    elif valittuseina.suunta == "ala":
                        seinalista.append(valittusolu.vas)
                        seinalista.append(valittusolu.oik)
                        seinalista.append(valittusolu.al)
                        valittusolu.oltujo = True

                        lapikaynti.append([valittusolu, valittuseina.suunta])

                    elif valittuseina.suunta == "vasen":
                        seinalista.append(valittusolu.vas)
                        seinalista.append(valittusolu.al)
                        seinalista.append(valittusolu.yl)
                        valittusolu.oltujo = True

                        lapikaynti.append([valittusolu, valittuseina.suunta])

                    elif valittuseina.suunta == "oikea":
                        seinalista.append(valittusolu.al)
                        seinalista.append(valittusolu.oik)
                        seinalista.append(valittusolu.yl)
                        valittusolu.oltujo = True

                        lapikaynti.append([valittusolu, valittuseina.suunta])

            seinalista.remove(valittuseina)

        return lapikaynti