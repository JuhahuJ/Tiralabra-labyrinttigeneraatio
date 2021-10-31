from random import choice
from ruudukko import Ruudukko


class Binaaripuu:
    """Luokka, jonka avulla luodaan labyrintti käyttäen binääripuualgoritmia."""

    def __init__(self, koko):
        self.koko = koko

    def luo_labyrintti(self):
        """Luo labyrintin käyttäen binääripuualgoritmia.

        Returns: Palauttaa listan, joka sisältää solu, suunta pareja, joiden perusteella labyrintti piirretään.
        """

        ruudukko = Ruudukko(self.koko)
        lapikaynti = []

        for i in range(len(ruudukko.ruudut)):
            for solu in ruudukko.ruudut[i]:
                suunta = choice(["alas", "oikealle"])
                lapikaynti.append([solu, suunta])

        return lapikaynti
