from PIL import Image
import numpy as np


# Zadanie 1:
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
    odjemnik = 255 / iterator

    while grubosc < z1 or grubosc < z2:
        ostatni_kolor -= odjemnik
        tablica[grubosc:z1, grubosc:z2] = ostatni_kolor
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        if ostatni_kolor < 0:
            ostatni_kolor = 0

    return tablica


def ramki_negatyw(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h) / dzielnik)
    tablica = np.zeros((h, w), dtype=np.uint8)
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
    odjemnik = 255 / iterator

    while grubosc < z1 or grubosc < z2:
        ostatni_kolor -= odjemnik
        tablica[grubosc:z1, grubosc:z2] = 255 - ostatni_kolor
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        if ostatni_kolor < 0:
            ostatni_kolor = 0

    return tablica


def wlasne(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h) / dzielnik)
    tablica = np.zeros((h, w), dtype=np.uint8)
    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    ostatni_kolor = 15
    while grubosc < z1 or grubosc < z2:
        tablica[grubosc:z1, grubosc:z2] = ostatni_kolor
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        ostatni_kolor += 15

    for wiersz in range(h // 20, h, h // 20):
        for kolumna in range(w // 20, w, w // 20):
            tablica[wiersz:wiersz + 3, kolumna:kolumna + 3] = 100

    np.fill_diagonal(tablica, 50)
    np.fill_diagonal(np.fliplr(tablica), 50)

    return tablica


def wlasne_negatyw(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h) / dzielnik)
    tablica = np.ones((h, w), dtype=np.uint8)
    tablica *= 255
    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    ostatni_kolor = 240
    while grubosc < z1 or grubosc < z2:
        tablica[grubosc:z1, grubosc:z2] = ostatni_kolor
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        ostatni_kolor -= 15

    for wiersz in range(h // 20, h, h // 20):
        for kolumna in range(w // 20, w, w // 20):
            tablica[wiersz:wiersz + 3, kolumna:kolumna + 3] = 255 - 100

    np.fill_diagonal(tablica, 255-50)
    np.fill_diagonal(np.fliplr(tablica), 255-50)

    return tablica


# Zadanie 1 ppkt a:
ramka = Image.fromarray(ramki(1000, 1000, 50))
ramka_negatyw = Image.fromarray(ramki_negatyw(1000, 1000, 50))
rysunek_wlasny = Image.fromarray(wlasne(1000, 1000, 25))
rysunek_wlasny_negatyw = Image.fromarray(wlasne_negatyw(1000, 1000, 25))


# Zadanie 1 ppkt b&c:
ramka.save('obraz1_1.jpg')
ramka.save('obraz1_1.png')
ramka_negatyw.save('obraz1_1N.jpg')
ramka_negatyw.save('obraz1_1N.png')
rysunek_wlasny.save('obraz1_2.jpg')
rysunek_wlasny.save('obraz1_2.png')
rysunek_wlasny_negatyw.save('obraz1_2N.jpg')
rysunek_wlasny_negatyw.save('obraz1_2N.png')


# Zadanie 2:
def pasy_rgb(w, h, dzielnik):
    GRUBOSC_STALA = int(w/dzielnik)
    tablica = np.zeros((h, w, 3), dtype=np.uint8)
    prawy_bok = GRUBOSC_STALA

    ostatni_kolor_z_palety_rgb = 0
    iterator = 0
    paleta_rgb_0 = [255, 0, 0]
    paleta_rgb_1 = [0, 255, 0]
    paleta_rgb_2 = [0, 0, 255]

    while prawy_bok <= w:
        iterator += 1
        lewy_bok = prawy_bok
        prawy_bok = lewy_bok + GRUBOSC_STALA

    lewy_bok = 0
    prawy_bok = GRUBOSC_STALA
    odjemnik = 255 / iterator
    tablica[:, :] = [paleta_rgb_0, paleta_rgb_1, paleta_rgb_2][ostatni_kolor_z_palety_rgb]
    ostatni_kolor_z_palety_rgb += 1

    while prawy_bok <= w:
        if ostatni_kolor_z_palety_rgb == 3:
            ostatni_kolor_z_palety_rgb = 0

        tablica[0:h, lewy_bok:prawy_bok] = [paleta_rgb_0, paleta_rgb_1, paleta_rgb_2][ostatni_kolor_z_palety_rgb]
        lewy_bok = prawy_bok
        prawy_bok = lewy_bok + GRUBOSC_STALA
        ostatni_kolor_z_palety_rgb += 1
        paleta_rgb_0[0] = paleta_rgb_0[0] - odjemnik
        paleta_rgb_1[1] = paleta_rgb_1[1] - odjemnik
        paleta_rgb_2[2] = paleta_rgb_2[2] - odjemnik

    return tablica


def pasy_rgb_negatyw(w, h, dzielnik):
    GRUBOSC_STALA = int(w / dzielnik)
    tablica = np.zeros((h, w, 3), dtype=np.uint8)
    prawy_bok = GRUBOSC_STALA

    ostatni_kolor_z_palety_rgb = 0
    iterator = 0
    paleta_rgb_0 = [0, 255, 255]
    paleta_rgb_1 = [255, 0, 255]
    paleta_rgb_2 = [255, 255, 0]

    while prawy_bok <= w:
        iterator += 1
        lewy_bok = prawy_bok
        prawy_bok = lewy_bok + GRUBOSC_STALA

    lewy_bok = 0
    prawy_bok = GRUBOSC_STALA
    odjemnik = 255 / iterator
    tablica[:, :] = [paleta_rgb_0, paleta_rgb_1, paleta_rgb_2][ostatni_kolor_z_palety_rgb]
    ostatni_kolor_z_palety_rgb += 1

    while prawy_bok <= w:
        if ostatni_kolor_z_palety_rgb == 3:
            ostatni_kolor_z_palety_rgb = 0

        tablica[0:h, lewy_bok:prawy_bok] = [paleta_rgb_0, paleta_rgb_1, paleta_rgb_2][ostatni_kolor_z_palety_rgb]
        lewy_bok = prawy_bok
        prawy_bok = lewy_bok + GRUBOSC_STALA
        ostatni_kolor_z_palety_rgb += 1
        paleta_rgb_0[0] = paleta_rgb_0[0] + odjemnik
        paleta_rgb_1[1] = paleta_rgb_1[1] + odjemnik
        paleta_rgb_2[2] = paleta_rgb_2[2] + odjemnik

    return tablica


# Zadanie 2 ppkt a:
img_pasy_rgb = Image.fromarray(pasy_rgb(1000, 1000, 50), mode='RGB')
img_pasy_rgb_negatyw = Image.fromarray(pasy_rgb_negatyw(1000, 1000, 50), mode='RGB')

img_pasy_rgb.save('obraz2.jpg')
img_pasy_rgb.save('obraz2.png')
img_pasy_rgb_negatyw.save('obraz2N.jpg')
img_pasy_rgb_negatyw.save('obraz2N.png')


# Zadanie 3:
def inicjaly_rgb(inicjaly):
    tab = np.asarray(inicjaly)
    tab = np.stack((np.array(tab),) * 3, -1)
    h, w = (tab.shape[0], tab.shape[1])
    tab = tab.astype(np.uint8)
    tab = tab * 255

    paleta_rgb_0 = [171, 26, 43]
    paleta_rgb_1 = [22, 117, 7]
    paleta_rgb_2 = [20, 95, 181]
    ostatni_kolor_z_palety_rgb = 0

    for wiersz in range(0, h - 1):
        for kolumna in range(0, w - 1):
            if (tab[wiersz][kolumna] == [0, 0, 0]).all():
                tab[wiersz][kolumna] = [paleta_rgb_0, paleta_rgb_1, paleta_rgb_2][ostatni_kolor_z_palety_rgb]

        ostatni_kolor_z_palety_rgb += 1
        if ostatni_kolor_z_palety_rgb == 3:
            ostatni_kolor_z_palety_rgb = 0

    return tab


obraz = Image.open("inicjaly.bmp")
obraz_inicjaly_rgb = inicjaly_rgb(obraz)
Image.fromarray(obraz_inicjaly_rgb).save('obraz3.jpg')
Image.fromarray(obraz_inicjaly_rgb).save('obraz3.png')
