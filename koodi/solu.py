from seina import Seina

class Solu:
    '''Solu olio, joka saa arvot x, y ja oltujo'''

    def __init__(self, y, x, oltujo=False, vas=None, oik=None, yl=None, al=None):
        self.x = x
        self.y = y
        self.oltujo = oltujo
        self.vas = vas
        self.oik = oik
        self.yl = yl
        self.al = al

    def luo_seinat(self):
        self.vas = Seina("vasen", self.x, self.y)
        self.oik = Seina("oikea", self.x, self.y)
        self.yl = Seina("ylä", self.x, self.y)
        self.al = Seina("ala", self.x, self.y)

    def koordinaatit(self):
        '''Palauttaa solun koordinaatit'''

        return [self.y, self.x]
