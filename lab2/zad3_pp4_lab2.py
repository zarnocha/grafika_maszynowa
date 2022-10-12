from PIL import Image  # Python Imaging Library
import numpy as np

def wlasne(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h)/dzielnik)
    tablica = np.zeros((h, w), dtype=np.uint8)
    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    ostatni_kolor = 1
    tablica[grubosc:z1, grubosc:z2] = ostatni_kolor
    while grubosc < z1 or grubosc < z2:
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        ostatni_kolor += 15
        tablica[grubosc:z1, grubosc:z2] = ostatni_kolor

    for wiersz in range(h//20, h, h//20):
        for kolumna in range(w//20, w, w//20):
            tablica[wiersz:wiersz+3, kolumna:kolumna+3] = 100

    np.fill_diagonal(tablica, 50)
    np.fill_diagonal(np.fliplr(tablica), 50)

    return tablica


rysunek_ramek = wlasne(300, 300, 20)
im_ramka = Image.fromarray(rysunek_ramek)
im_ramka.show()