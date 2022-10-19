from PIL import Image
import numpy as np


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
    ostatni_kolor = 245
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


rysunek_wlasny = Image.fromarray(wlasne(1000, 1000, 25))
rysunek_wlasny_negatyw = Image.fromarray(wlasne_negatyw(1000, 1000, 25))

rysunek_wlasny.save('obrazek1_2.jpg')
rysunek_wlasny.save('obrazek1_2.png')
rysunek_wlasny_negatyw.save('obrazek1_2N.jpg')
rysunek_wlasny_negatyw.save('obrazek1_2N.png')
