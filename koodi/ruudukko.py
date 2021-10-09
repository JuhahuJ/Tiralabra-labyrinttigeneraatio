from solu import Solu


class Ruudukko:
    def __init__(self,koko:int,ruudut=[]):
        self.koko = koko
        self.ruudut = ruudut
        

    def luo(self):
        self.ruudut = []
        for i in range(self.koko):
            self.ruudut.append("väliaikainen arvo")
            apulista = []
            for j in range(self.koko):
                solus = Solu(i, j)
                apulista.append(solus)
            self.ruudut[i] = apulista
        