import unittest
from solu import Solu
from ruudukko import Ruudukko

class TestSoluJaRuudukko(unittest.TestCase):
    def setUp(self):
        self.yksisolu = Solu(5,6)
        self.vainruudukko = Ruudukko(5)
        self.vainruudukko.luo()

    def test_solussa_ei_kayty_luodessa(self):
        self.assertEqual(self.yksisolu.oltujo, False)

    def test_solun_koordinaatit_oikeat(self):
        self.assertEqual(self.yksisolu.koordinaatit(), (5,6))

    def test_ruudukossa_on_oikea_maara_soluja(self):
        ruutulaskuri = 0
        for i in range(len(self.vainruudukko.ruudut)):
            for j in range(len(self.vainruudukko.ruudut[i])):
                ruutulaskuri += 1
        self.assertEqual(ruutulaskuri,25)

    def test_ruudukon_soluissa_ei_olla_kayty(self):
        jossainkayty = False
        for i in range(len(self.vainruudukko.ruudut)):
            for j in range(len(self.vainruudukko.ruudut[i])):
                if self.vainruudukko.ruudut[i][j].oltujo == True:
                    jossainkayty = True
        self.assertEqual(jossainkayty,False)
        self.vainruudukko.ruudut[0][3].oltujo = True
        for i in range(len(self.vainruudukko.ruudut)):
            for j in range(len(self.vainruudukko.ruudut[i])):
                if self.vainruudukko.ruudut[i][j].oltujo == True:
                    jossainkayty = True
        self.assertEqual(jossainkayty,True)