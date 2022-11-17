from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

im = Image.open('baby_yoda.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)
# im.show()


def zakres(w, h):  # funkcja, która uprości podwójna petle for
    return [(i, j) for i in range(w) for j in range(h)]


# ***********************************************************************************************************************8
# zmiana wartości pikseli za pomocą metod getpixel i putpixel
def pobierz_kolor_pixela(obraz, m, n):  # m, n współrzędne punktu na obrazie
    w, h = obraz.size
    if m < w and n < h: # ograniczenia w i h
        kolor = obraz.getpixel((m, n))
    return kolor


print(pobierz_kolor_pixela(im, 260, 200))


def wstaw_pixel_w_punkt(obraz, m, n, kolor):  # m, n współrzędne punktu na obrazie, kolor -  dane pixela do wstawienia
    w, h = obraz.size
    if m < w and n < h:     # zabez. zakresu
        obraz.putpixel((m, n), kolor)
    return obraz


def wstaw_pixel_w_zakresie(obraz, m, n, kolor, w_z, h_z):  # w miejscu m,n wstawia kwadrat o boku 100 w kolorze "kolor"
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            obraz.putpixel((i + m, j + n), kolor)
    return obraz


def rozjasnij_obraz_putpixel(obraz, a, b, c):  # zmienia wartości każdego kanału
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w, h):
        p = obraz.getpixel((i, j))  # pobieramy z oryg. obrazu a wstawiamy do skopiowanego
        obraz1.putpixel((i, j), (p[0] + a, p[1] + b, p[2] + c)) # na kazdym kanale inaczej sie rozjasnia
    return obraz1


def rozjasnij_obraz_w_zakresie(obraz, m, n, a, b, c, w_z, h_z):  # w miejscu m,n "rozjaśnia" prostokat o wymiaraxh w_z, h_z
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i + m < w and j + n < h:
            p = obraz.getpixel((i + m, j + n))
            obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c))
    return obraz1


def skopiuj_obraz_w_zakresie(obraz, m, n, m1, n1, w_z, h_z):  # kopiuje prostokat o wymiarach w_z, h_z z miejsca m,n i wstawia w miejscu m1,n1
    obraz1 = obraz.copy()
    w, h = obraz.size
    for i, j in zakres(w_z, h_z):
        if i+m < w and j+n < h:
            p = obraz.getpixel((i + m, j + n))
            if i + m1 < w and j + n1 < h:
                obraz1.putpixel((i + m1, j + n1), p)
    return obraz1

# dokladnie zadanie 2 ktore jest do zrobienia
def rozjasnij_obraz_z_maska(obraz, maska, m, n, a, b, c):  # w miejscu m, n zmienia tylko te pixele, które odpowiadają czarnym pixelom maski, maska jest obrazem czarnobiałym
    obraz1 = obraz.copy()
    w, h = obraz.size
    w0, h0 = maska.size
    for i, j in zakres(w0, h0):
        if i + m < w and j + n < h:
            if maska.getpixel((i, j)) == 0: # tam gdzie czarne to rozjasnij
                p = obraz.getpixel((i + m, j + n))
                obraz1.putpixel((i + m, j + n), (p[0] + a, p[1] + b, p[2] + c)) # funkcja rozjasniania
    return obraz1


def dodaj_szum(obraz, n, kolor1, kolor2):  # dodawanie szumu typu salt and pepper
    w, h = obraz.size
    x, y = np.random.randint(0, w, n), np.random.randint(0, h,
                                                         n)  # powtarza n razy losowanie z zakresu 0,w i z zakresu 0,h
    for (i, j) in zip(x, y):  # zip robi pary z list x,y
        obraz.putpixel((i, j), (kolor1 if np.random.rand() < 0.5 else kolor2))  # salt-and-pepper
    return obraz


#
im1 = im.copy()
im2 = im.copy()
im3 = im.copy()
im4 = im.copy()
im5 = im.copy()
maska = Image.open('gwiazdka.bmp')
im6 = im.copy()

plt.title("1. wstaw_pixel_w_zakresie")
plt.axis('off')
plt.imshow(wstaw_pixel_w_zakresie(im1, 200, 100, (200, 200, 200), 100, 100))
plt.show()

plt.title("2. rozjasnij_obraz_putpixel")
plt.axis('off')
plt.imshow(rozjasnij_obraz_putpixel(im2, 50, 20, -10))
plt.show()

plt.title("3. rozjasnij_obraz_w_zakresie")
plt.axis('off')
plt.imshow(rozjasnij_obraz_w_zakresie(im3, 200,100, 50, 20, -10, 100, 100))
plt.show()

plt.title("4. skopiuj_obraz_w_zakresie")
plt.axis('off')
plt.imshow(skopiuj_obraz_w_zakresie(im4, 70, 300, 240, 200, 60, 60))
plt.show()

plt.title("4.1 skopiuj_obraz_w_zakresie")
plt.axis('off')
plt.imshow(skopiuj_obraz_w_zakresie(im4, 40, 300, 750, 500, 100, 100))
plt.show()

plt.title("5. rozjasnij_obraz_z_maska")
plt.axis('off')
plt.imshow(rozjasnij_obraz_z_maska(im5, maska, 200, 100, 50, 20, -10))
plt.show()


plt.title("6.  dodaj_szum")
plt.axis('off')
plt.imshow(dodaj_szum(im6, 50000, (0, 0, 0), (255, 255, 255)))
plt.show()


# ****************************************************************
# zmiana wartości pikseli za pomocą metody  load


# funkcja wykorzystująca inne funkcje na wartościach pikseli
def zastosuj_funkcje(image, func):
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = func(pixele[i, j])


def przestaw_kolory(pixel):
    return (pixel[1], pixel[2], pixel[0])


def filtr_liniowy(image, a, b): # a, b liczby całkowite
    w, h = image.size
    pixele = image.load()
    for i, j in zakres(w, h):
        pixele[i, j] = (pixele[i, j][0]* a + b, pixele[i, j][1]* a + b, pixele[i, j][2]* a + b)


im7 = im.copy()
zastosuj_funkcje(im7, przestaw_kolory)
plt.title("7. Metoda load i funkcja przestaw_kolory  ")
plt.axis('off')
plt.imshow(im7)
plt.show()

im8 = im.copy()
filtr_liniowy(im8, 2, -100)
plt.title("8. Metoda load i funkcja filtr_liniowy ")
plt.axis('off')
plt.imshow(im8)
plt.show()

# ****************************************************************


# zmiana wartości pikseli za pomocą metody  point
# obraz ktory chce dostac w zad 5
im9 = im.copy()
im9 = im9.point(lambda i: i + 100)
plt.title("9.  Metoda point - rozjasnij ")
plt.axis('off')
plt.imshow(im9)
plt.show()


# ****************************************************************

# obcięcie wartości pixeli do pewnej wartości wsp

def efekt_plakatu(im, wsp):
    return im.point(lambda
                        i: i > wsp and 255)  # sztuczka Pythona - jeżeli nieprawda, że i > wsp wstaw 0 a w przeciwnym przypadku wstaw 255


def efekt_plakatu_rownowaznie(im, wsp):
    r, g, b = im.split()
    # każdy z kanałow zmieniamy na obraz czarnobiały w trybie "L"
    r1 = r.point(lambda i: i > wsp and 255)
    r1.show()
    g1 = g.point(lambda i: i > wsp and 255)
    b1 = b.point(lambda i: i > wsp and 255)
    return Image.merge("RGB", (r1, g1, b1))


plt.title("10.   Metoda point - efekt plakatu ")
plt.axis('off')
plt.imshow(efekt_plakatu(im, 100))
plt.show()
# --------------------

# dlaczego poniższe polececiania nie rozjasniaja obrazu tak jak funkcja "rozjaśnij"
obraz = im.copy()
T = np.array(obraz, dtype='uint8')
T += 100
obraz_wynik = Image.fromarray(T, "RGB")
plt.title("11.   Zmiana wartosci tablicy ")
plt.axis('off')
plt.imshow(obraz_wynik)
plt.show()
