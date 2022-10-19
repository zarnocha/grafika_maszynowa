from PIL import Image
import numpy as np


def ramki(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h) / dzielnik)
    tablica = np.ones((h, w, 3), dtype=np.uint8)
    tablica = tablica * 255
    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc

    ostatni_kolor_z_palety_rgb = 0
    iterator = 0
    paleta_rgb_0 = [255, 0, 0]
    paleta_rgb_1 = [0, 255, 0]
    paleta_rgb_2 = [0, 0, 255]

    while grubosc < z1 or grubosc < z2:
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        iterator += 1

    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    odjemnik = 255 / iterator

    tablica[:, :] = [paleta_rgb_0, paleta_rgb_1, paleta_rgb_2][ostatni_kolor_z_palety_rgb]
    ostatni_kolor_z_palety_rgb += 1

    while grubosc < z1 or grubosc < z2:
        if ostatni_kolor_z_palety_rgb == 3:
            ostatni_kolor_z_palety_rgb = 0

        tablica[grubosc:z1, grubosc:z2] = [paleta_rgb_0, paleta_rgb_1, paleta_rgb_2][ostatni_kolor_z_palety_rgb]
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        ostatni_kolor_z_palety_rgb += 1
        paleta_rgb_0[0] = paleta_rgb_0[0] - odjemnik
        paleta_rgb_1[1] = paleta_rgb_1[1] - odjemnik
        paleta_rgb_2[2] = paleta_rgb_2[2] - odjemnik

    return tablica


def ramki_negatyw(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h) / dzielnik)
    tablica = np.ones((h, w, 3), dtype=np.uint8)
    tablica = tablica * 255
    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc

    ostatni_kolor_z_palety_rgb = 0
    iterator = 0
    paleta_rgb_0 = [0, 255, 255]
    paleta_rgb_1 = [255, 0, 255]
    paleta_rgb_2 = [255, 255, 0]

    while grubosc < z1 or grubosc < z2:
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        iterator += 1

    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    odjemnik = 255 / iterator

    tablica[:, :] = [paleta_rgb_0, paleta_rgb_1, paleta_rgb_2][ostatni_kolor_z_palety_rgb]
    ostatni_kolor_z_palety_rgb += 1

    while grubosc < z1 or grubosc < z2:
        if ostatni_kolor_z_palety_rgb == 3:
            ostatni_kolor_z_palety_rgb = 0

        tablica[grubosc:z1, grubosc:z2] = [paleta_rgb_0, paleta_rgb_1,  paleta_rgb_2][ostatni_kolor_z_palety_rgb]
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        ostatni_kolor_z_palety_rgb += 1
        paleta_rgb_0[0] = paleta_rgb_0[0] + odjemnik
        paleta_rgb_1[1] = paleta_rgb_1[1] + odjemnik
        paleta_rgb_2[2] = paleta_rgb_2[2] + odjemnik

    return tablica


ramka = Image.fromarray(ramki(1000, 1000, 50), mode='RGB')
ramka_negatyw = Image.fromarray(ramki_negatyw(1000, 1000, 50), mode='RGB')

ramka.show()
ramka_negatyw.show()
