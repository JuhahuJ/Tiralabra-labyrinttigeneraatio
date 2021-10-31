from random import randrange, choice
from oliot.ruudukko import Ruudukko


class Syvyyshaku:
    """Luokka, jonka avulla luodaan labyrintti käyttäen satunnaista syvyyshakua."""

    def __init__(self, koko):
        self.koko = koko

    def luo_labyrintti(self):
        """Luo labyrintin käyttäen satunnaista syvyyshakua.

        Returns: Palauttaa listan, joka sisältää peräkkäisiä soluja, joiden perusteella labyrintti piirretään.
        """
        ruudukko = Ruudukko(self.koko)
        lapikaynti = []
        aloitusruutu = ruudukko.ruudut[randrange(
            self.koko)][randrange(self.koko)]
        aloitusruutu.oltujo = True
        solulista = [aloitusruutu]

        while len(solulista) > 0:
            nykyinensolu = solulista[-1]
            viereiset = ruudukko.viereiset_solut(nykyinensolu)
            lapikaynti.append(nykyinensolu)
            solulista.pop()

            if len(viereiset) > 0:
                solulista.append(nykyinensolu)
                seuraavasolu = choice(viereiset)
                seuraavasolu.oltujo = True
                solulista.append(seuraavasolu)

        return lapikaynti
