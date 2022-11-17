import numpy as np
from PIL import Image, ImageChops
import matplotlib.pyplot as plt

# Zadanie 1
obraz = Image.open('obraz.jpg')
inicjaly = Image.open('inicjaly.bmp')


# Zadanie 2.1
def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def wstaw_inicjaly(obraz, inicjaly, m, n, kolor):
    if m < 0 or n < 0:
        return "Złe współrzędne."

    obraz1 = obraz.copy()
    w0, h0 = inicjaly.size
    w, h = obraz1.size

    for i, j in zakres(w0, h0):
        p = inicjaly.getpixel((i, j))
        if i + m < w and j + n < h:
            if p == 0:
                obraz1.putpixel((i + m, j + n), kolor)
            else:
                obraz1.putpixel((i + m, j + n), (255, 255, 255))
    return obraz1


wstaw_inicjaly(obraz, inicjaly, 400, 450, (255, 0, 0)).show()
wstaw_inicjaly(obraz, inicjaly, 400, 450, (255, 0, 0)).save('obraz1.jpg')


# Zadanie 2.2
def wstaw_inicjaly_maska(obraz, inicjaly, m, n, x, y, z):
    if m < 0 or n < 0:
        return "Złe współrzędne."

    obraz1 = obraz.copy()
    w, h = obraz1.size
    w0, h0 = inicjaly.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if inicjaly.getpixel((i, j)) == 0:
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (p[0] + x, p[1] + y, p[2] + z))
    return obraz1


wstaw_inicjaly_maska(obraz, inicjaly, 200, 225, 100, 100, -100).show()
wstaw_inicjaly_maska(obraz, inicjaly, 200, 225, 100, 100, -100).save('obraz2.jpg')


# Zadanie 3
def wstaw_inicjaly_load(obraz, inicjaly, m, n, kolor):
    w0, h0 = inicjaly.size
    w, h = obraz.size
    obraz1 = obraz.copy()
    pixele_obrazu = obraz1.load()
    pixele_inicjalow = inicjaly.load()

    for i, j in zakres(w0, h0):
        p = pixele_inicjalow[i, j]
        if i + m < w and j + n < h:
            if p == 0:
                pixele_obrazu[i + m, j + n] = kolor
            else:
                pixele_obrazu[i + m, j + n] = (255, 255, 255)

    return obraz1


wstaw_inicjaly_load(obraz, inicjaly, 400, 450, (255, 0, 0)).show()


def wstaw_inicjaly_maska_load(obraz, inicjaly, m, n, x, y, z):
    w0, h0 = inicjaly.size
    w, h = obraz.size
    obraz1 = obraz.copy()
    inicjaly1 = inicjaly.copy()
    pixele_obrazu = obraz1.load()
    pixele_inicjalow = inicjaly1.load()

    for i, j in zakres(w0, h0):
        p = pixele_inicjalow[i, j]
        if i + m < w and j + n < h:
            if p == 0:
                pixele_obrazu[i + m, j + n] = (pixele_obrazu[i + m, j + n][0] + x, pixele_obrazu[i + m, j + n][1] + y, pixele_obrazu[i + m, j + n][2] + z)

    return obraz1


wstaw_inicjaly_maska_load(obraz, inicjaly, 200, 225,  100, 100, -100).show()


# Zadanie 4.1
def kontrast(obraz, wsp_kontrastu):
    if wsp_kontrastu not in range(0, 101):
        return 'Zły wsp. kontrastu'

    mn = ((255 + wsp_kontrastu) / 255) ** 2
    obraz1 = obraz.copy()
    return obraz1.point(lambda i: 128 + (i-128) * mn)


plt.figure(figsize=(8, 12))

plt.subplot(4, 3, 2)
plt.imshow(kontrast(obraz, 0))
plt.title('Kontrast:\n0')
plt.axis('off')

plt.subplot(4, 3, 4)
plt.imshow(kontrast(obraz, 10))
plt.title('Kontrast:\n10')
plt.axis('off')

plt.subplot(4, 3, 6)
plt.imshow(kontrast(obraz, 30))
plt.title('Kontrast:\n30')
plt.axis('off')

plt.subplot(4, 3, 7)
plt.imshow(kontrast(obraz, 50))
plt.title('Kontrast:\n50')
plt.axis('off')

plt.subplot(4, 3, 9)
plt.imshow(kontrast(obraz, 70))
plt.title('Kontrast:\n70')
plt.axis('off')

plt.subplot(4, 3, 10)
plt.imshow(kontrast(obraz, 90))
plt.title('Kontrast:\n90')
plt.axis('off')

plt.subplot(4, 3, 12)
plt.imshow(kontrast(obraz, 100))
plt.title('Kontrast:\n100')
plt.axis('off')

plt.subplots_adjust(wspace=0.05, hspace=0.5)
# plt.savefig('kontrast.png')
plt.show()


# Zadanie 4.2
def transformacja_logarytmiczna(obraz):
    obraz1 = obraz.copy()
    return obraz1.point(lambda i: 255 * np.log(1 + (i / 255)))


transformacja_logarytmiczna(obraz).show()
# transformacja_logarytmiczna(obraz).save('transformacja_logarytmiczna.jpg')


# Zadanie 4.3
def transformacja_gamma(obraz, gamma):
    if gamma < 0:
        return 'Zły wsp. gamma'

    obraz1 = obraz.copy()
    return obraz1.point(lambda i: (i/255) ** (1/gamma) * 255)


plt.figure(figsize=(5, 5))

plt.subplot(2, 3, 1)
plt.imshow(transformacja_gamma(obraz, 0.1))
plt.title('Transformacja\ngamma: 0.1')
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(transformacja_gamma(obraz, 0.5))
plt.title('Transformacja\ngamma: 0.5')
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(transformacja_gamma(obraz, 1))
plt.title('Transformacja\ngamma: 1')
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(transformacja_gamma(obraz, 5))
plt.title('Transformacja\ngamma: 5')
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(transformacja_gamma(obraz, 10))
plt.title('Transformacja\ngamma: 10')
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(transformacja_gamma(obraz, 20))
plt.title('Transformacja\ngamma: 20')
plt.axis('off')

plt.subplots_adjust(wspace=0.1, hspace=0.5)
# plt.savefig('transformacja_gamma.png')
plt.show()


# Zadanie 5
T = np.array(obraz, dtype='uint8')

obraz_wynik = Image.fromarray(T, "RGB")
obraz_wynik.show()

obraz_wynik = obraz.point(lambda i: i + 100)
obraz_wynik.show()


# Zadanie 6
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


pointer = obraz.point(lambda i: i + 100)
# pointer.save('zad6_pointer.jpg')
tablica = tablica_jak_pointer(obraz, 100)
# tablica.save('zad6_tablica.jpg')
roznica = ImageChops.difference(pointer, tablica)
# roznica.save('zad6_roznica.jpg')
print(f'np.array(roznica).any(): {np.array(roznica).any()}')
