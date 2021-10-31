from copy import copy
from oliot.solu import Solu


class Ruudukko:
    '''Ruudukko olio, jolle annetaan koko ja joka sisältää solut ruudukossa.'''

    def __init__(self, koko: int, ruudut=[]):
        self.koko = koko
        self.ruudut = ruudut
        self.luo()

    def luo(self):
        """Luo ruudukon annetun koon perusteella"""

        self.ruudut = []

        for i in range(self.koko):
            self.ruudut.append("väliaikainen arvo")
            apulista = []

            for j in range(self.koko):
                solu = Solu(i, j)
                apulista.append(solu)

            self.ruudut[i] = apulista

    def viereiset_solut(self, solu):
        """Tarkistaa annetun solun ympärillä olevat solut
        
        Args:
            solu: Solu, jonka viereiset solut halutaan saada selville.

        Returns: Palauttaa listan soluja, jotka ovat ruudukossa ja joissa ei olla käyty.
        """

        viereiset = []

        if solu.y > 0 and self.ruudut[solu.y-1][solu.x].oltujo is False:
            viereiset.append(self.ruudut[solu.y-1][solu.x])

        if solu.y < len(self.ruudut)-1 and self.ruudut[solu.y+1][solu.x].oltujo is False:
            viereiset.append(self.ruudut[solu.y+1][solu.x])

        if solu.x > 0 and self.ruudut[solu.y][solu.x-1].oltujo is False:
            viereiset.append(self.ruudut[solu.y][solu.x-1])

        if solu.x < len(self.ruudut)-1 and self.ruudut[solu.y][solu.x+1].oltujo is False:
            viereiset.append(self.ruudut[solu.y][solu.x+1])

        return viereiset

    def vastakkainen_seina(self, seina):
        """Tarkistaa annetun seinän vastapuolen koordinaatit.
        
        Args:
            seina: Seinä, jonka toisen koordinaatit halutaan tietää.

        Returns: Palauttaa annetun seinän vastakkaisen seinän.
        """

        vastakkainen_seina = copy(seina)
        if seina.suunta == "ylä":
            vastakkainen_seina.y -= 1
            return vastakkainen_seina

        if seina.suunta == "ala":
            vastakkainen_seina.y += 1
            return vastakkainen_seina

        if seina.suunta == "vasen":
            vastakkainen_seina.x -= 1
            return vastakkainen_seina

        if seina.suunta == "oikea":
            vastakkainen_seina.x += 1
            return vastakkainen_seina
