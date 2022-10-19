from PIL import Image
import numpy as np


def pasy_rgb(w, h, dzielnik):
    GRUBOSC_STALA = int(w/dzielnik)
    tablica = np.zeros((h, w, 3), dtype=np.uint8)
    lewy_bok = 0
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
    lewy_bok = 0
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


img_pasy_rgb = Image.fromarray(pasy_rgb(1000, 1000, 50), mode='RGB')
img_pasy_rgb_negatyw = Image.fromarray(pasy_rgb_negatyw(1000, 1000, 50), mode='RGB')

img_pasy_rgb.show()
img_pasy_rgb_negatyw.show()

img_pasy_rgb.save('obraz2.jpg')
img_pasy_rgb.save('obraz2.png')
img_pasy_rgb_negatyw.save('obraz2N.jpg')
img_pasy_rgb_negatyw.save('obraz2N.png')
