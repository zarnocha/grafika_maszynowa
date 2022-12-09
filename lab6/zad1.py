import numpy as np
from PIL import Image


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def rysuj_prostokat(obraz, m, n, a, b, kolor):
    if m < 0 or n < 0:
        return "Złe współrzędne."

    obraz1 = obraz.copy()
    pixele_obrazu = obraz1.load()
    w, h = obraz1.size

    for i in range(0, a):
        if m+i < w:
            pixele_obrazu[m+i, n] = kolor

    for i in range(0, a):
        for j in range(0, b, b-1):
            if m+i < w and n+j < h:
                pixele_obrazu[m+i, n+j] = kolor

    for j in range(0, b):
        if n+j < w:
            pixele_obrazu[m, n+j] = kolor

    for j in range(0, b):
        if m+a < w and n+j < h:
            pixele_obrazu[m+a, n+j] = kolor

    return obraz1


def rysuj_kwadrat(obraz, m, n, a, kolor):
    if m < 0 or n < 0:
        return "Złe współrzędne."
    if m <
    m = int(m/2)
    n = int(n/2)

    obraz1 = obraz.copy()
    pixele_obrazu = obraz1.load()
    w, h = obraz1.size

    for i in range(0, a):
        if m + i < w:
            pixele_obrazu[m + i, n] = kolor

    for i in range(0, a):
        for j in range(0, a, a - 1):
            if m + i < w and n + j < h:
                pixele_obrazu[m + i, n + j] = kolor

    for j in range(0, a):
        if n + j < w:
            pixele_obrazu[m, n + j] = kolor

    for j in range(0, a):
        if m + a < w and n + j < h:
            pixele_obrazu[m + a, n + j] = kolor

    return obraz1


def rysuj_kwadrat_grubosc(obraz, m, n, a, kolor, grubosc):
    if m < 0 or n < 0:
        return "Złe współrzędne."

    obraz1 = obraz.copy()
    pixele_obrazu = obraz1.load()
    w, h = obraz1.size

    for i in range(0, a):
        for g in range(0, grubosc):
            if m + i < w:
                pixele_obrazu[m + i, n + g] = kolor

    for i in range(0, a):
        for g in range(0, grubosc):
            if m + i < w and n + g < h:
                pixele_obrazu[m + g, n + i] = kolor

    for j in range(0, a + grubosc):
        for g in range(0, grubosc):
            pixele_obrazu[m + j, n + a + g] = kolor

    for j in range(0, a):
        for g in range(0, grubosc):
            if m + a < w and n + j < h:
                pixele_obrazu[m + a + g, n + j] = kolor

    return obraz1



im = Image.open('../lab5/moodle_lab5/baby_yoda.jpg')
# rysuj_prostokat(im, 300, 100, 250, 150, (255, 0, 0)).show()
rysuj_kwadrat(im, 0, 0, 250, (255, 0, 0)).show()
# rysuj_kwadrat_grubosc(im, 290, 3, 250, (255, 0, 0), 133).show()