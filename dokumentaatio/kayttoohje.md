# Käyttöohje

Ohjelman käyttöä varten täytyy olla poetry asennettuna.

Kun poetry on asennettu ohjelman riippuvuudet voi asentaa komennolla:

```bash
poetry install
```

## Ohjelman käyttö

Kun riippuvuudet on asennettu ohjelman voi suorittaa komennolla:

```bash
poetry run invoke start
```

Ohjelma aukeaa aloitusruutuun jossa on 4 painikettä.

Yläoikealta voi valita minkä kokoisen labyrintin haluaa luoda.

Kokovalinnan lisäksi löytyy kolme labyrinttigeneraatiovaihtoehtoa.

Nämä ovat algoritmit, joiden avulla labyrintin voi luoda.

Kun on valinnut minkä kokoisen labyrintin haluaa luoda ja algoritmin jolla se luodaan päästään ruutuun, jossa on labyrintti, joka on luotu valitulla algoritmilla.

Ylimmästä nappulasta pääsee takaisin algoritmi- ja kokovalintaan. Luodun labyrintin kokoa ei voi muuttaa muualla, kuin aloitusruudussa.

Keskimmäisestä napista voi luoda uuden samankokoisen labyrintin, joka on luotu samalla algoritmilla.

Alhaalla olevista napeista voi tarkkailla algoritmin luomisprosessia. Oikeanpuoleinen nappi on luomisen nopeus sekunteina per tapahtuma ja 
vasemmanpuoleinen nappula aloittaa läpikäynnin.
