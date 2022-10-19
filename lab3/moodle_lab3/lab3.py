from PIL import Image  # Python Imaging Library
import numpy as np


# obrazy w odcieniach szarości
def rysuj_ramke_szare(w, h, dzielnik, kolor_ramki, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor_ramki  # wypełnienie tablicy szarym kolorem o wartości kolor_ramki
    grub = int(min(w, h) / dzielnik)  # wyznaczenie grubości  ramki
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2] = kolor  # wypełnienie podtablicy kolorem o wartości kolor
    return tab


tab = rysuj_ramke_szare(120, 60, 8, 100, 200)
im_ramka = Image.fromarray(tab)
im_ramka.show()


def rysuj_pasy_poziome_szare(w, h, dzielnik, zmiana_koloru):  # w, h   -  rozmiar obrazu
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(h / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                tab[i, j] = (k * zmiana_koloru) % 256
    return tab


tab1 = rysuj_pasy_poziome_szare(300, 200, 100, 10)
obraz1 = Image.fromarray(tab1)
obraz1.show()


def negatyw_szare(tab):  # tworzy tablicę dla negatywu
    h, w = tab.shape
    tab_neg = tab.copy()
    for i in range(h):
        for j in range(w):
            tab_neg[i, j] = 255 - tab[i, j]
    return tab_neg


tab_neg = negatyw_szare(tab1)
obraz_neg = Image.fromarray(tab_neg)
obraz_neg.show()


def rysuj_po_przekatnej_szare(w):  # rysuje kwadratowy obraz
    t = (w, w)
    tab = np.zeros(t, dtype=np.uint8)
    for i in range(w):
        for j in range(w):
            tab[i, j] = (i + j) % 256
    return tab


tab = rysuj_po_przekatnej_szare(512)
im = Image.fromarray(tab)
im.show()


def rysuj_ramki_szare(w, zmiana_koloru):
    t = (w, w)
    tab = np.zeros(t, dtype=np.uint8)
    kolor = 255 - int(w / 2) + 1
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = kolor
        kolor = kolor + zmiana_koloru
    return tab


tab = rysuj_ramki_szare(300, 5)
im = Image.fromarray(tab)
im.show()


# obrazy kolorowe
def rysuj_ramke_kolor(w, h, dzielnik, kolor_ramki, kolor):  # kolor_ramki, kolor podajemy w postaci [r, g, b]
    t = (h, w, 3)  # rozmiar tablicy
    tab = np.ones(t, dtype=np.uint8)  # deklaracja tablicy
    tab[:] = kolor_ramki  # wypełnienie tablicy kolorem czerwonym
    grub = int(min(w, h) / dzielnik)  # wyznaczenie grubości  ramki
    z1 = h - grub
    z2 = w - grub
    tab[grub:z1, grub:z2, 0] = kolor[0]  # wypełnienie wartości kanału R liczbą r
    tab[grub:z1, grub:z2, 1] = kolor[1]  # wypełnienie wartości kanału G liczbą g
    tab[grub:z1, grub:z2, 2] = kolor[2]  # wypełnienie wartości kanału R liczbą r
    # tab[grub:z1, grub:z2] = kolor # wersja równoważna
    return tab


tab = rysuj_ramke_kolor(120, 60, 8, [0, 0, 255], [100, 200, 0])
im_ramka = Image.fromarray(tab)
im_ramka.show()


def rysuj_pasy_poziome_3kolory(w, h, dzielnik):  # funkcja rysuje pasy poziome na przemian czerwony, zielony, niebieski
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    grub = int(h / dzielnik)
    for k in range(dzielnik):
        for g in range(grub):
            i = k * grub + g
            for j in range(w):
                if k % 3 == 0:
                    tab[i, j] = [255, 0, 0]
                elif k % 3 == 1:
                    tab[i, j] = [0, 255, 0]
                else:
                    tab[i, j] = [0, 0, 255]
    return tab


tab1 = rysuj_pasy_poziome_3kolory(300, 200, 20)
obraz1 = Image.fromarray(tab1)
obraz1.show()


def rysuj_pasy_poziome_kolor(w, h, dzielnik, kolor,
                             zmiana_koloru):  # funkcja rysuje pasy poziome, przy czym kazda składowa koloru zwieksza się o "zmiana_koloru"
    t = (h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    tab[:] = kolor
    grub = int(h / dzielnik)
    for k in range(dzielnik):
        r = (kolor[0] + k * zmiana_koloru) % 256
        g = (kolor[1] + k * zmiana_koloru) % 256
        b = (kolor[2] + k * zmiana_koloru) % 256
        for m in range(grub):
            i = k * grub + m
            for j in range(w):
                tab[i, j] = [r, g, b]
    return tab


tab1 = rysuj_pasy_poziome_kolor(300, 200, 20, [100, 200, 0], 32)
obraz1 = Image.fromarray(tab1)
obraz1.show()


def koloruj_obraz(obraz, kolor):
    t_obraz = np.asarray(obraz)
    h, w = t_obraz.shape
    t =(h, w, 3)
    tab = np.ones(t, dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if t_obraz[i, j] == False:
                tab[i, j] = kolor
            else:
                tab[i, j] = [255, 255, 255]
    return tab

gwiazdka = Image.open("lab3/gwiazdka.bmp")
obraz2 = Image.fromarray(koloruj_obraz(gwiazdka, [120, 240, 50]))
obraz2.show()

def rysuj_ramki_kolorowe(w, zmiana_koloru_r, zmiana_koloru_g, zmiana_koloru_b):
    t = (w, w, 3)
    tab = np.zeros(t, dtype=np.uint8)
    kolor_r = 0
    kolor_g = 0
    kolor_b = 0
    z = w
    for k in range(int(w / 2)):
        for i in range(k, z - k):
            for j in range(k, z - k):
                tab[i, j] = [kolor_r, kolor_g, kolor_b]
        kolor_r = kolor_r + zmiana_koloru_r
        kolor_g = kolor_g + zmiana_koloru_g
        kolor_b = kolor_b + zmiana_koloru_b
    return tab


tab = rysuj_ramki_kolorowe(300, 2, 4, 6)
obraz3 = Image.fromarray(tab)
obraz3.show()