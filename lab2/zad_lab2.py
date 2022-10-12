from PIL import Image
import numpy as np


# Zadanie 1:
def wstaw_obraz(obraz_wstawiany, w_m, h_m, wsp):
    if wsp < 1:
        return "Ten wspolczynnik jest zbyt niski"

    tab_obrazu = np.asarray(obraz_wstawiany)
    h0, w0 = tab_obrazu.shape
    h1, w1 = (int(h0 * wsp), int(w0 * wsp))
    tab = np.zeros((h1, w1), dtype=np.uint8)

    if w_m < 0 or h_m < 0:
        return "Nieprawidlowe umiejscowienie wstawianego obrazu"

    for wiersz in range(h_m, h_m + h0 - 1):
        for kolumna in range(w_m, w_m + w0 - 1):
            if kolumna > w1 - 1 or wiersz > h1 - 1:
                continue
            else:
                tab[wiersz][kolumna] = tab_obrazu[wiersz - h_m][kolumna - w_m]

    tab = tab.astype(bool)
    po_wstawieniu = Image.fromarray(tab)
    return po_wstawieniu


obraz = Image.open("inicjaly.bmp")

# Zadanie 2:
wstaw_obraz(obraz, 50, 25, 2).save("wstawianie1.bmp")
wstaw_obraz(obraz, 150, 45, 3).save("wstawianie2.bmp")
wstaw_obraz(obraz, 400, 200, 5).save("wstawianie3.bmp")


# Zadanie 3 ppkt 1:
def ramki(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h) / dzielnik)
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


# Zadanie 3 ppkt 2:
def pasy(w, h, dzielnik):
    GRUBOSC_STALA = int(w / dzielnik)
    tablica = np.zeros((h, w), dtype=np.uint8)
    h0, w0 = tablica.shape
    grubosc = GRUBOSC_STALA * 2
    lewy_bok = GRUBOSC_STALA
    while grubosc <= w0:
        tablica[0:h0, lewy_bok:grubosc] = 1
        lewy_bok += 2 * GRUBOSC_STALA
        grubosc = lewy_bok + GRUBOSC_STALA

    return tablica * 255


# Zadanie 3 ppkt 3:
def styk(w, h, m, n):
    tablica = np.ones((h, w), dtype=np.uint8)
    tablica[0: n, 0:m] = 0
    tablica[n:h, m:w] = 0
    return tablica * 255


# Zadanie 3 ppkt 4:
def wlasne(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h) / dzielnik)
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

    for wiersz in range(h // 20, h, h // 20):
        for kolumna in range(w // 20, w, w // 20):
            tablica[wiersz:wiersz + 3, kolumna:kolumna + 3] = 100

    np.fill_diagonal(tablica, 50)
    np.fill_diagonal(np.fliplr(tablica), 50)

    return tablica


# Zadanie 3 ppkt 5:
Image.fromarray(ramki(480, 320, 8)).save("ramki.bmp")
Image.fromarray(pasy(480, 320, 8)).save("pasy.bmp")
Image.fromarray(styk(480, 320, 100, 50)).save("styk.bmp")
Image.fromarray(wlasne(480, 320, 8)).save("wlasne.bmp")
