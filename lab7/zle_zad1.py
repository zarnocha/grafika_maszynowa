import numpy as np
from PIL import Image, ImageFilter, ImageChops

im = Image.open('obraz.jpg')


def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def filtruj(obraz, kernel, scale):
    w, h = obraz.size
    kopia = obraz.copy()
    tab_obraz = obraz.load()
    tab_kopia = kopia.load()
    pomin = False

    if scale != 0:
        for x, y in zakres(len(kernel), len(kernel)):
            # print(kernel[x][y])
            # print(x-1, y-1)
            kernel[x][y] = kernel[x][y] / scale

    for i, j in zakres(w, h):
        if i == 0 and j == 0:
            i += 1
            j += 1
            pomin = True

        if j == 0:
            j += 1
            pomin = True
        if i == 0:
            i += 1
            pomin = True

        if j == w:
            i += 1
            pomin = True

        if i == h:
            pomin = True
            break

        # print(i, j)
        if not pomin:
            tmp_tab = np.zeros((len(kernel), len(kernel)), dtype=object)
            for x, y in zakres(len(kernel), len(kernel)):
                tmp_rgb = []
                for rgb in range(0, 3):
                    tmp_rgb.append(int(kernel[x][y] * tab_obraz[x - 1, y - 1][rgb]))
                tmp_tab[x, y] = tmp_rgb

            suma = [0, 0, 0]
            for x in zakres(len(tmp_tab), len(tmp_tab)):
                for rgb in range(0, 3):
                    suma[rgb] += tmp_tab[x][rgb]

            # print(tab_kopia[i,j])
            # print(tuple(suma))
            tab_kopia[i, j] = tuple(suma)
        pomin = False

    return kopia


#
# blur_moj = filtruj(im,
#                    [[1, 1, 1, 1, 1],
#                     [1, 0, 0, 0, 1],
#                     [1, 0, 0, 0, 1],
#                     [1, 0, 0, 0, 1],
#                     [1, 1, 1, 1, 1]],
#                    1)
#
# blur_moj.show()

test = filtruj(im,
               [
                   [0, 0, 0],
                   [0, 1, 0],
                   [0, 0, 0]
               ], 1)

test.show()
# ImageChops.difference(im, blur_moj).show()
# print(ImageFilter.BLUR.filterargs)
# blur = im.filter(ImageFilter.BLUR)
# blur.show()
