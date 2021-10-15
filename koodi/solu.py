class Solu:
    '''Solu olio, joka saa arvot x, y ja oltujo'''

    def __init__(self, y, x, oltujo=False):
        self.x = x
        self.y = y
        self.oltujo = oltujo

    def koordinaatit(self):
        '''Palauttaa solun koordinaatit'''
        
        return (self.y, self.x)
