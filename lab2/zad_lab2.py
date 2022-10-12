from PIL import Image  # Python Imaging Library
import numpy as np


def wstaw_obraz(obraz_wstawiany, w_m, h_m, wsp):
    if wsp < 1:
        return "Ten wspolczynnik jest zbyt niski"

    tab_obrazu = np.asarray(obraz_wstawiany)
    h0, w0 = tab_obrazu.shape  # wymiary wstawianego obrazu
    h1, w1 = (int(h0 * wsp), int(w0 * wsp))  # wymiary przeskalowanej tablicy
    tab = np.zeros((h1, w1), dtype=np.uint8)

    if w_m < 0 or h_m < 0:
        return "Nieprawidlowe umiejscowienie wstawianego obrazu"

    for wiersz in range(h_m, h_m + h0-1):
        for kolumna in range(w_m, w_m + w0 - 1):
            if kolumna > w1 - 1 or wiersz > h1 - 1:
                continue
            else:
                tab[wiersz][kolumna] = tab_obrazu[wiersz - h_m][kolumna - w_m]

    tab = tab.astype(bool)
    po_wstawieniu = Image.fromarray(tab)
    # po_wstawieniu.show()
    return po_wstawieniu
    # po_wstawieniu.save('zad_lab2.bmp')


obraz = Image.open("inicjaly.bmp")
# wstaw_obraz(obraz, 50, 25, 2).show()
wstaw_obraz(obraz, 150, 45, 2).show()
