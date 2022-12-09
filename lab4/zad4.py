import numpy as np
from PIL import Image
from matplotlib import pyplot as plt


# Zadanie 4
def wlasne(w, h, dzielnik):
    GRUBOSC_STALA = int(min(w, h) / dzielnik)
    tablica = np.zeros((h, w), dtype=np.uint8)
    grubosc = GRUBOSC_STALA
    z1 = h - grubosc
    z2 = w - grubosc
    ostatni_kolor = 1
    tablica[grubosc:z1, grubosc:z2] = ostatni_kolor
    while grubosc < z1 or grubosc < z2:
        grubosc += GRUBOSC_STALA
        z1 -= GRUBOSC_STALA
        z2 -= GRUBOSC_STALA
        ostatni_kolor += 15
        tablica[grubosc:z1, grubosc:z2] = ostatni_kolor

    for wiersz in range(h // 20, h, h // 20):
        for kolumna in range(w // 20, w, w // 20):
            tablica[wiersz:wiersz + 3, kolumna:kolumna + 3] = 100

    np.fill_diagonal(tablica, 50)
    np.fill_diagonal(np.fliplr(tablica), 50)

    return tablica


im4 = Image.fromarray(wlasne(500, 500, 30), mode='L')

# ppkt a.
im1 = Image.open('obraz.jpg')
r, g, b = im1.split()

im_r = Image.merge('RGB', (im4, g, b))
im_g = Image.merge('RGB', (r, im4, b))
im_b = Image.merge('RGB', (r, g, im4))

# ppkt b.
plt.figure(figsize=(41, 31))

plt.subplot(1, 3, 1)
plt.imshow(im_r)
plt.title('Własny obraz jako R', fontsize=60)
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(im_g)
plt.title('Własny obraz jako G', fontsize=60)
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(im_b)
plt.title('Własny obraz jako B', fontsize=60)
plt.axis('off')

plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('fig2.png')
plt.show()
