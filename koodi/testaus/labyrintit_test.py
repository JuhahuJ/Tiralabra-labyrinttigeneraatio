import unittest
from labyrintit.syvyyshaku import Syvyyshaku
from labyrintit.binaaripuu import Binaaripuu
from labyrintit.prim import Prim

class TestLabyrintit(unittest.TestCase):
    def setUp(self):
        self.binaari = Binaaripuu(5).luo_labyrintti()
        self.syvyys = Syvyyshaku(5).luo_labyrintti()
        self.prim = Prim(5).luo_labyrintti()

    def test_binaari_luo_oikean_kokoisen_labyrintin(self):
        self.assertEqual(len(self.binaari),25)
