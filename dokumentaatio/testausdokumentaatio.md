#Ohjelman testaus ja testikattavuusraportti

Ohjelman testaus on suoritettu Pytestillä, jonka avulla on luotu myös testikattavuusraportti.
Sen saa auki htmlcov kansiosta avaamalla tiedoston index.html. 
Testikattavuusraportin voi luoda myös uudelleen poetryn avulla komennoilla:

```bash
poetry run coverage run --branch -m pytest
```

```bash
poetry run coverage html
```

Huom! Poetryn pitää olla asennettuna!
