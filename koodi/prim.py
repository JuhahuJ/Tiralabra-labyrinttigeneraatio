from ruudukko import Ruudukko
from random import choice

ruudukko = Ruudukko(5)
ruudukko.luo()

apulista = []

solu = ruudukko.ruudut[0][0]
solu.oltujo = True
apulista.append(solu.vas)
apulista.append(solu.oik)
apulista.append(solu.yl)
apulista.append(solu.al)

while len(apulista) > 0:
    valittuseina = choice(apulista)
    vastakkainenseina = ruudukko.vastakkainen_seina(valittuseina)
    if  vastakkainenseina.y > -1 and vastakkainenseina.y < ruudukko.koko and vastakkainenseina.x > -1 and vastakkainenseina.x < ruudukko.koko:
        valittusolu = ruudukko.ruudut[ruudukko.vastakkainen_seina(valittuseina).y][ruudukko.vastakkainen_seina(valittuseina).x]
        if valittusolu.oltujo is not solu.oltujo:
            if valittuseina.suunta == "ylä":
                apulista.append(valittusolu.vas)
                apulista.append(valittusolu.oik)
                apulista.append(valittusolu.yl)
                valittusolu.oltujo = True
            elif valittuseina.suunta == "ala":
                apulista.append(valittusolu.vas)
                apulista.append(valittusolu.oik)
                apulista.append(valittusolu.al)
                valittusolu.oltujo = True
            elif valittuseina.suunta == "vasen":
                apulista.append(valittusolu.vas)
                apulista.append(valittusolu.al)
                apulista.append(valittusolu.yl)
                valittusolu.oltujo = True
            elif valittuseina.suunta == "oikea":
                apulista.append(valittusolu.al)
                apulista.append(valittusolu.oik)
                apulista.append(valittusolu.yl)
                valittusolu.oltujo = True
            solu = valittusolu
    
    apulista.remove(valittuseina)
    

for i in range(len(ruudukko.ruudut)):
    for j in ruudukko.ruudut[i]:
        print(j.oltujo)