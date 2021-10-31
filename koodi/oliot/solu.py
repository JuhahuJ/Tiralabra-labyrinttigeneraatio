class Solu:
    '''Solu olio, joka saa koordinaatit y ja x ja arvon oltujo ja neljä seinää.'''

    def __init__(self, y, x, oltujo=False, vas=None, oik=None, yl=None, al=None):
        self.x = x
        self.y = y
        self.oltujo = oltujo
        self.vas = vas
        self.oik = oik
        self.yl = yl
        self.al = al
        self.luo_seinat()

    def luo_seinat(self):
        """Luo seinät, jotka kuuluvat solulle."""

        self.vas = Seina("vasen", self.y, self.x)
        self.oik = Seina("oikea", self.y, self.x)
        self.yl = Seina("ylä", self.y, self.x)
        self.al = Seina("ala", self.y, self.x)


class Seina:
    """Seinä olio, jolla on suunta ja koordinaatit y ja x"""

    def __init__(self, suunta, y, x):
        self.suunta = suunta
        self.x = x
        self.y = y
