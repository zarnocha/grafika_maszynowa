from PIL import Image
import numpy as np


def pasy(w, h, dzielnik):
    GRUBOSC_STALA = int(w/dzielnik)
    tablica = np.zeros((h, w), dtype=np.uint8)
    h0, w0 = tablica.shape
    grubosc = GRUBOSC_STALA*2
    lewy_bok = GRUBOSC_STALA
    while grubosc <= w0:
        tablica[0:h0, lewy_bok:grubosc] = 1
        lewy_bok += 2 * GRUBOSC_STALA
        grubosc = lewy_bok + GRUBOSC_STALA

    return tablica * 255


rysunek_ramek = pasy(156, 284, 12)
im_ramka = Image.fromarray(rysunek_ramek)
im_ramka.show()
