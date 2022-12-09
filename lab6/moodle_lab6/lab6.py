from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('lab5/baby_yoda.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)
#im.show()

def odbij_lewa_strone_na_prawo(im):
    img = im.copy()
    w, h = im.size
    w1 = int(w / 2)
    px = img.load()
    for i in range(w1, w):
        for j in range(h):
            px[i, j] = px[w - i, j]
    return img

odbij_lewa_strone_na_prawo(im).show()

def odbij_w_pionie(im):
    px0 = im.load()
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px0[w - 1 - i, j]
    return img
odbij_w_pionie(im).show()


def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]

def rysuj_kolo(obraz, m_s, n_s, r, kolor):
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w, h):
        if (i-m_s)**2+(j-n_s)**2 < r**2: # wzór na koło o środku (m_s, n_s) i promieniu r
            obraz1.putpixel((i,j), kolor)
    return obraz1

obraz = rysuj_kolo(im, 100, 100, 50, (200,0,0))
obraz.show()

import math
def rysuj_okrag(obraz, a, b ,r, kolor):
    w,h =obraz.size
    for angle in range(0,360,1):
        x = int(r * math.sin(angle) + a)
        y = int(r * math.cos(angle) + b)
        if x <w and y<h:
            obraz.putpixel((x,y), kolor)
    return obraz

rysuj_okrag(im, 100, 100, 30, (0, 200,0)).show()
# ***********************************************************************************************************************8
