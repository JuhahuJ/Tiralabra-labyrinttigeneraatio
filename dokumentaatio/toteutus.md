# Toteutus

## Kaikille labyrinttialgoritmeille yleistä

Kaikkien algoritmien toteutuksessa käytetään luokkia Ruudukko ja Solu ja kaikki algoritmit aloittavat luomalla ruudukon.
Ruudukko luokka tekee matriisin soluista, joille annetaan koordinaatit sen mukaan, missä kohtaa matriisia ne ovat.

Soluilla on myös arvo oltujo, jota käytetään, kun halutaan tietää onko jossakin solussa käyty jo labyrintin luomisen aikana.
Sen lisäksi solulla on myös neljä seinää, joilla on samat koordinaatit kuin solulla ja suunta suhteessa soluun.

Ruudukossa on myös funktiot viereiset solut, ja vastakkainen seinä.

Viereiset solut palauttaa listan kaikisa annettua solua ympäröivistä seinistä ottaen huomioon, ettei mukaan tule ruudukon ulkopuoleisia soluja, jotka eivät ole olemassa.

Vastakkainen seinä palauttaa seinän, joka on annetun seinän toisella puolella, mutta antaa myös seiniä, jotka eivät kuulu ruudukkoon.

Sovelluksen käyttöliittymässä käytetään tkinteriä.

## Satunnainen syvyyshaku

Algoritmi aloittaa valitsemalla satunnaisen aloitusruudun ja merkkaamalla sen käydyksi.

Sen jälkeen se tarkistaa viereiset solut ja valitsee niistä jonkin jossa ei olla käyty.

Sama toistuu kunnes päädytään tilanteeseen, jossa ei ole saatavilla viereisiä soluja, joissa ei olla käyty.

Sitten peruutetaan takaisin kunnes löytyy kohta, jossa on käymättömiä viereisiä soluja ja toistetaan, kunnes kaikki ruudukon solut on käyty läpi.

## Primin algoritmi

Algoritmi aloittaa valitsemalla satuunaisen aloitusruudun ja merkkaamalla sen käydyksi.

Tämän jälkeen algoritmmi lisää valitun solun seinät listalle.

Listalta valitaan satunnainen seinä, jonka takaiselta solulta tarkistetaan oltujo.

Jos solussa ei olla käyty sen seinät lukuunottamatta sitä, jonka kautta solu löytyi, lisätään listaan ja samaa toistetaan kunnes kaikissa soluissa ollaan käyty.

## Binääripuualgoritmi

Algoritmi alkaa ruudukon vasemmasta yläkulmasta koordinaateista 0, 0.

Se käy yksitellen läpi jokaisen ruudukon solun ja valitsee jokaisessa joko alas tai oikealle.

Kun valinta on tehty valitussa suunnassa oleva seinä poistetaan.

Ruudukon alareunassa algoritmi voi valita vin oikealle ja vastaavasti oikeassa reunassa algoritmi voi valita vain alas.

## Kiinnostavaa

Algoritmeista "kevyin" oli binääripuualgoritmi ja raskain primin algoritmi.
Binääripuuta luodessa 10000 kertaa 20 * 20 ruudukolla aikaa kului alle 12 sekuntia.
Vastaavasti syvyyshaulla aikaa kului yli 24 sekuntia ja primin algoritmilla kului lähes 135 sekuntia.
Tarkemmat luvut ovat testausdokumentissa.

Sama pätee myös algoritmien viemään tilaan.
Binääripuuta luodessa ei tarvitse pitää muistissa mitään muuta, kuin suunta, josta seinä poistetaan.
Syvyyshaussa pidetään muistissa reitti, joka ollaan kuljettu ja primin algoritmissa pidetään muistissa solujen seiniä.

## Lähteet

https://en.wikipedia.org/wiki/Maze_generation_algorithm

http://weblog.jamisbuck.org/2011/2/1/maze-generation-binary-tree-algorithm#
