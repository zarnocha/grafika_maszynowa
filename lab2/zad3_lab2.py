from PIL import Image
import numpy as np


def ramki(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h)/dzielnik)
    tablica = np.zeros((h, w), dtype=np.uint8)
    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    ostatni_kolor = 1
    tablica[grubosc:z1, grubosc:z2] = ostatni_kolor
    while grubosc < z1 or grubosc < z2:
        if ostatni_kolor == 0:
            ostatni_kolor = 1
        else:
            ostatni_kolor = 0

        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        tablica[grubosc:z1, grubosc:z2] = ostatni_kolor

    return tablica * 255


rysunek_ramek = ramki(500, 500, 20)
im_ramka = Image.fromarray(rysunek_ramek)
im_ramka.show()
