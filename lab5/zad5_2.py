import numpy as np
from PIL import Image

obraz = Image.open('obraz.jpg')


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def tablica_jak_pointer(obraz, zmienna):
    obraz1 = obraz.copy()
    w, h = obraz.size
    pixele_obrazu = obraz1.load()
    for i, j in zakres(w, h):
        p = [*pixele_obrazu[i, j]]
        if p[0] + zmienna >= 255:
            p[0] = 255
        else:
            p[0] = p[0] + zmienna

        if p[1] + zmienna >= 255:
            p[1] = 255
        else:
            p[1] += zmienna

        if p[2] + zmienna >= 255:
            p[2] = 255
        else:
            p[2] += zmienna

        pixele_obrazu[i, j] = tuple(p)

    return obraz1


tablica_jak_pointer(obraz, 100).show()