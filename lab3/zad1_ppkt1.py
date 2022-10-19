from PIL import Image
import numpy as np


def ramki(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h) / dzielnik)
    tablica = np.ones((h, w), dtype=np.uint8)
    tablica = tablica * 255
    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    ostatni_kolor = 255
    iterator = 0

    while grubosc < z1 or grubosc < z2:
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        iterator += 1

    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    odjemnik = 255 / iterator  # co ile odejmować

    while grubosc < z1 or grubosc < z2:
        ostatni_kolor -= odjemnik
        tablica[grubosc:z1, grubosc:z2] = ostatni_kolor
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        if ostatni_kolor < 0:  # zabezpiecz. aby w środku był kolor czarny jeżeli zmienna ostatni_kolor spadłaby poniżej 0
            ostatni_kolor = 0

    return tablica


def ramki_negatyw(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h) / dzielnik)
    tablica = np.zeros((h, w), dtype=np.uint8)  # zmieniamy tablice na np.zeros, aby miec czarne tło/ramki
    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    ostatni_kolor = 255
    iterator = 0

    while grubosc < z1 or grubosc < z2:
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        iterator += 1

    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    odjemnik = 255 / iterator  # co ile odejmować

    while grubosc < z1 or grubosc < z2:
        ostatni_kolor -= odjemnik
        tablica[grubosc:z1, grubosc:z2] = 255 - ostatni_kolor  # aby uzyskać kolory jaśniejsze, np. 255 - 250 = 5 -> kolor o 5 jaśniejszy od białego, itd.
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        if ostatni_kolor < 0:  # zabezpiecz. aby w środku był kolor czarny jeżeli zmienna ostatni_kolor spadłaby poniżej 0
            ostatni_kolor = 0

    return tablica


ramka = Image.fromarray(ramki(1000, 1000, 50))
ramka_negatyw = Image.fromarray(ramki_negatyw(1000, 1000, 50))

ramka.save('obraz1_1.jpg')
ramka.save('obraz1_1.png')
ramka_negatyw.save('obraz1_1N.jpg')
ramka_negatyw.save('obraz1_1N.png')
