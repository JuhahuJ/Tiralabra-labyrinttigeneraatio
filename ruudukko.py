from solu import solu


class ruudukko:
    def __init__(self,koko:int,ruudut=[]):
        self.koko = koko
        self.ruudut = ruudut
        

    def luo(self):
        for i in range(self.koko):
            self.ruudut.append("väliaikainen arvo")
            apulista = []
            for j in range(self.koko):
                solus = solu(i, j)
                apulista.append(solus)
            self.ruudut[i] = apulista
        