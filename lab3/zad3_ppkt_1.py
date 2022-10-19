from PIL import Image  # Python Imaging Library
import numpy as np


def wlasne_rgb(inicjaly):
    tab = np.asarray(inicjaly)
    tab = np.stack((np.array(tab),) * 3, -1)    # metoda z internetu na zmienienie tablicy 2d na 3d, z szarosci na RGB
    h, w, z = tab.shape
    tab = tab.astype(np.uint8)
    tab = tab * 255

    paleta_rgb_0 = [255, 0, 0]
    paleta_rgb_1 = [0, 255, 0]
    paleta_rgb_2 = [0, 0, 255]
    ostatni_kolor_z_palety_rgb = 0

    for wiersz in range(0, h - 1):
        for kolumna in range(0, w - 1):
            print(f'w{wiersz} k{kolumna}')
            if (tab[wiersz][kolumna] == [0, 0, 0]).all():   # sprawdzamy czy kolor sie zgadza
                tab[wiersz][kolumna] = [paleta_rgb_0, paleta_rgb_1, paleta_rgb_2][ostatni_kolor_z_palety_rgb]

        ostatni_kolor_z_palety_rgb += 1     # kolor jest zmieniany co wiersz, wiec koloruje wierszami
        if ostatni_kolor_z_palety_rgb == 3:
            ostatni_kolor_z_palety_rgb = 0

    return tab


obraz = Image.open("inicjaly.bmp")
wlasne_rgb(obraz).save('obraz3.jpg')
wlasne_rgb(obraz).save('obraz3.png')
