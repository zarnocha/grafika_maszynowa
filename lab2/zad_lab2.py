from PIL import Image   # Python Imaging Library
import numpy as np

def wstaw_obraz(obraz_wstawiany, w_m, h_m, wsp):
    if wsp < 1:
        return "Ten wspolczynnik jest zbyt niski"

    tab_obrazu = np.asarray(obraz_wstawiany)
    tab_obrazu = tab_obrazu * 1
    h0, w0 = tab_obrazu.shape # wielkosc wstawianego obrazu
    h1, w1 = (int(h0 * wsp), int(w0 * wsp)) # wielkosc przeskalowanej tablicy
    tab = np.zeros((h1, w1))

    if w_m > w1 or h_m > h1 or w_m < 0 or h_m < 0:
        return "Nieprawidlowe umiejscowienie wstawianego obrazu"

    for wiersz in range(w_m, w1-1):
        for kolumna in range(h_m, h1):
            print(f'wiersz: {wiersz}, kolumna: {kolumna}')
            tab[wiersz][kolumna] = tab_obrazu[wiersz-w_m][kolumna-h_m]

    tab.astype(bool)

    po_wstawieniu = Image.fromarray(tab)

    po_wstawieniu.show()


obraz = Image.open("lab2/inicjaly.bmp")


wstaw_obraz(obraz, 0, 0, 2)