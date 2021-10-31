import unittest
from oliot.solu import Solu
from oliot.ruudukko import Ruudukko


class TestSoluJaRuudukko(unittest.TestCase):
    def setUp(self):
        self.yksisolu = Solu(5, 6)
        self.vainruudukko = Ruudukko(5)

    def test_solussa_ei_kayty_luodessa(self):
        self.assertEqual(self.yksisolu.oltujo, False)

    def test_solun_koordinaatit_oikeat(self):
        self.assertEqual((self.yksisolu.y, self.yksisolu.x), (5, 6))

    def test_ruudukossa_on_oikea_maara_soluja(self):
        ruutulaskuri = 0
        for i in range(len(self.vainruudukko.ruudut)):
            for j in range(len(self.vainruudukko.ruudut[i])):
                ruutulaskuri += 1
        self.assertEqual(ruutulaskuri, 25)

    def test_ruudukon_soluissa_ei_olla_kayty(self):
        jossainkayty = False
        for i in range(len(self.vainruudukko.ruudut)):
            for j in range(len(self.vainruudukko.ruudut[i])):
                if self.vainruudukko.ruudut[i][j].oltujo == True:
                    jossainkayty = True
        self.assertEqual(jossainkayty, False)
        self.vainruudukko.ruudut[0][3].oltujo = True
        for i in range(len(self.vainruudukko.ruudut)):
            for j in range(len(self.vainruudukko.ruudut[i])):
                if self.vainruudukko.ruudut[i][j].oltujo == True:
                    jossainkayty = True
        self.assertEqual(jossainkayty, True)

    def test_viereiset_solut_palauttaa_oikeat_solut(self):
        viereiset = self.vainruudukko.viereiset_solut(self.vainruudukko.ruudut[1][2])
        self.assertEqual([viereiset[0].y,viereiset[0].x,viereiset[1].y,viereiset[1].x,viereiset[2].y,viereiset[2].x,viereiset[3].y,viereiset[3].x,], [0, 2, 2, 2, 1, 1, 1, 3])
        viereiset2 = self.vainruudukko.viereiset_solut(self.vainruudukko.ruudut[0][3])
        self.assertEqual([viereiset2[0].y,viereiset2[0].x,viereiset2[1].y,viereiset2[1].x,viereiset2[2].y,viereiset2[2].x], [1, 3, 0, 2, 0, 4])
        viereiset3 = self.vainruudukko.viereiset_solut(self.vainruudukko.ruudut[2][0])
        self.assertEqual([viereiset3[0].y,viereiset3[0].x,viereiset3[1].y,viereiset3[1].x,viereiset3[2].y,viereiset3[2].x], [1, 0, 3, 0, 2, 1])
        viereiset4 = self.vainruudukko.viereiset_solut(self.vainruudukko.ruudut[4][4])
        self.assertEqual([viereiset4[0].y,viereiset4[0].x,viereiset4[1].y,viereiset4[1].x], [3, 4, 4, 3])

    def test_vastakkainen_seina_palauttaa_oikean_seinan(self):
        vastakkainen = self.vainruudukko.vastakkainen_seina(self.vainruudukko.ruudut[0][2].al)
        self.assertEqual(vastakkainen.y, 1)
        vastakkainen2 = self.vainruudukko.vastakkainen_seina(self.vainruudukko.ruudut[3][0].yl)
        self.assertEqual(vastakkainen2.y, 2)
        vastakkainen3 = self.vainruudukko.vastakkainen_seina(self.vainruudukko.ruudut[4][2].vas)
        self.assertEqual(vastakkainen3.x, 1)
        vastakkainen4 = self.vainruudukko.vastakkainen_seina(self.vainruudukko.ruudut[0][2].oik)
        self.assertEqual(vastakkainen4.x, 3)