from labyrintit.syvyyshaku import Syvyyshaku
from labyrintit.binaaripuu import Binaaripuu
from labyrintit.prim import Prim

def test_binaari_1():
    Binaaripuu(5).luo_labyrintti()

def test_binaari_2():
    Binaaripuu(10).luo_labyrintti()

def test_binaari_3():
    Binaaripuu(20).luo_labyrintti()

def test_syvyys_1():
    Syvyyshaku(5).luo_labyrintti()

def test_syvyys_2():
    Syvyyshaku(10).luo_labyrintti()

def test_syvyys_3():
    Syvyyshaku(20).luo_labyrintti()

def test_prim_1():
    Prim(5).luo_labyrintti()

def test_prim_2():
    Prim(10).luo_labyrintti()

def test_prim_3():
    Prim(20).luo_labyrintti()

if __name__ == "__main__":
    import timeit
    print("Kun 5 * 5 labyrintti luodaan binääripuualgoritmilla 10000 kertaa, aikaa kuluu:",timeit.timeit("test_binaari_1()", setup="from __main__ import test_binaari_1", number=10000), "sekuntia")
    print("Kun 10 * 10 labyrintti luodaan binääripuualgoritmilla 10000 kertaa, aikaa kuluu:",timeit.timeit("test_binaari_2()", setup="from __main__ import test_binaari_2", number=10000), "sekuntia")
    print("Kun 20 * 20 labyrintti luodaan binääripuualgoritmilla 10000 kertaa, aikaa kuluu:",timeit.timeit("test_binaari_3()", setup="from __main__ import test_binaari_3", number=10000), "sekuntia")
    print("Kun 5 * 5 labyrintti luodaan syvyyshakualgoritmilla 10000 kertaa, aikaa kuluu:",timeit.timeit("test_syvyys_1()", setup="from __main__ import test_syvyys_1", number=10000), "sekuntia")
    print("Kun 10 * 10 labyrintti luodaan syvyyshakualgoritmilla 10000 kertaa, aikaa kuluu:",timeit.timeit("test_syvyys_2()", setup="from __main__ import test_syvyys_2", number=10000), "sekuntia")
    print("Kun 20 * 20 labyrintti luodaan syvyyshakualgoritmilla 10000 kertaa, aikaa kuluu:",timeit.timeit("test_syvyys_3()", setup="from __main__ import test_syvyys_3", number=10000), "sekuntia")
    print("Kun 5 * 5 labyrintti luodaan primin algoritmilla 10000 kertaa, aikaa kuluu:",timeit.timeit("test_prim_1()", setup="from __main__ import test_prim_1", number=10000), "sekuntia")
    print("Kun 10 * 10 labyrintti luodaan primin algoritmilla 10000 kertaa, aikaa kuluu:",timeit.timeit("test_prim_2()", setup="from __main__ import test_prim_2", number=10000), "sekuntia")
    print("Kun 20 * 20 labyrintti luodaan primin algoritmilla 10000 kertaa, aikaa kuluu:",timeit.timeit("test_prim_3()", setup="from __main__ import test_prim_3", number=10000), "sekuntia")
