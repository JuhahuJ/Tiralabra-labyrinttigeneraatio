import timeit
from labyrintit.syvyyshaku import Syvyyshaku
from labyrintit.binaaripuu import Binaaripuu
from labyrintit.prim import Prim

binaari = Binaaripuu(5).luo_labyrintti()
syvyys = Syvyyshaku(5).luo_labyrintti()
prim = Prim(5).luo_labyrintti()

if __name__ == "__main__":
    print(prim)