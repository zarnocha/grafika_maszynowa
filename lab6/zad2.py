import numpy as np
from PIL import Image


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def zakres_odwrotny(w, h):
    return [(i, j) for i in range(w-1, 0, -1) for j in range(h-1, 0, -1)]


def odbij_gora_dol(obraz):
    w, h = obraz.size
    obraz_tab = obraz.load()

    kopia = obraz.copy()
    kopia_tab = kopia.load()

    x, y = (0, 0)

    for i in range(w-1, -1, -1):
        y = 0
        for j in range(h-1, -1, -1):
            kopia_tab[x, y] = obraz_tab[i, j]
            y += 1
        x += 1

    return kopia


def odbij_dol_na_gore(obraz):
    obraz_tab = np.asarray(obraz)
    kopia_tab = obraz_tab.copy()
    w, h = obraz.size
    p_w, p_h = (int(w/2), int(h/2))

    if w % 2 != 0:
        p_w += 1

    if h % 2 != 0:
        p_h += 1

    kopia_tab[0:p_h-1, 0:w] = obraz_tab[p_h:h, 0:w][::-1]

    return Image.fromarray(kopia_tab)


def odbij_gore_na_dol(obraz):
    obraz_tab = np.asarray(obraz)
    kopia_tab = obraz_tab.copy()
    w, h = obraz.size
    p_w, p_h = (int(w / 2), int(h / 2))

    if w % 2 != 0:
        p_w += 1

    if h % 2 != 0:
        p_h += 1

    kopia_tab[p_h-1:h, 0:w] = obraz_tab[0:p_h, 0:w][::-1]

    return Image.fromarray(kopia_tab)


im = Image.open('moodle_lab6/baby_yoda (kopia).jpg')
# odbij_gora_dol(im).show()
# odbij_dol_na_gore(im).show()
# odbij_gore_na_dol(im).show()


# 2.4
def odbij_w_pionie(im):
    px0 = im.load()
    img = im.copy()
    w, h = im.size
    px = img.load()
    for i in range(w):
        for j in range(h):
            px[i, j] = px0[w - 1 - i, j]
            px[i, j] = px[w - 1 - i, j]
    return img


# odbij_w_pionie(im).show()


def rysuj_kolo(obraz, m_c, n_c, m_s, n_s, r, kolor):
    obraz1 = obraz.copy()
    w, h = obraz.size
    pixele = []

    for i, j in zakres(w, h):
        if (i - m_c) ** 2 + (j - n_c) ** 2 < r ** 2:  # wzór na koło o środku (m_s, n_s) i promieniu r
            pixele.append(obraz.getpixel((i, j)))

    x = 0
    for i, j in zakres(w, h):
        if (i - m_s) ** 2 + (j - n_s) ** 2 < r ** 2:  # wzór na koło o środku (m_s, n_s) i promieniu r
            obraz1.putpixel((i, j), pixele[x])
            x += 1

    return obraz1


ob = rysuj_kolo(im, 96, 347, 100, 100, 34, (255, 0, 0))
ob = rysuj_kolo(ob, 96, 347, 476, 194, 22, (255, 0, 0))
ob = rysuj_kolo(ob, 96, 347, 361, 151, 21, (255, 0, 0))
ob.show()
ob.save('yoda.jpg')