import numpy as np
from PIL import Image, ImageChops
from matplotlib import pyplot as plt

# Zadanie 1
im1 = Image.open('obraz.jpg')

# ----------------------------------------------------------------------------------------------------------------------------

# Zadanie 2
# ppkt a.
tablica_obrazu = np.array(im1)

# kanały R, G, B w zmiennych t_r, t_g, t_b
t_r = tablica_obrazu[:, :, 0]
t_g = tablica_obrazu[:, :, 1]
t_b = tablica_obrazu[:, :, 2]

# obrazy powstałe z osobnych kanałów R, G, B do zmiennych im_r, im_g, im_b
im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)

# zapis obrazów do plików im_r.jpg, im_g.jpg, im_b.jpg
im_r.save('im_r.jpg')
im_g.save('im_g.jpg')
im_b.save('im_b.jpg')

# ppkt b.
im2 = Image.merge('RGB', (im_r, im_g, im_b))
im1_2_roznica = ImageChops.difference(im1,
                                      im2)  # wniosek: obrazy są takie same, bo obraz powstały z różnic jest cały czarny i jego tablica nie ma ani jednego nieczarnego piksela (oznaczającego, że byłaby różnica)
im1_2_roznica.show()
print(f'Czy jakikolwiek piksel z obrazu różnicy obrazów im2 i im1 jest nieczarny: {np.array(im1_2_roznica).any()}')

# ppkt c.
porownanie = (np.array(im2) == np.array(im1)).all()
print(
    f'Czy tablice obrazów im2 i im1 mają te same wartości na tych samych pozycjach: {porownanie}')  # printowane jest True, zatem obraz nie ma żadnych różnic w pikselach.

# ----------------------------------------------------------------------------------------------------------------------------

# Zadanie 3
im1 = Image.open('obraz.jpg')
r, g, b = im1.split()  # rozdzielenie kanałów RGB z obraz.jpg do zmiennych r, g, b.
im3 = Image.merge('RGB', (b, r, g))  # tworzenie obrazu z permutacji kanałów

# ppkt a.
im3.save('im3.jpg')  # zapis obrazu powstałego z permutacji do plików o rozszerzeniach JPG i PNG
im3.save('im3.png')

# ppkt b.
im3_jpg = Image.open('im3.jpg')
im3_png = Image.open('im3.png')
im3_jpg_png_roznica = ImageChops.difference(im3_jpg, im3_png)   # tworzenie obrazu różnic przy tym samym obrazie ale o innych rozszerzeniach
im3_jpg_png_roznica.show()
print(f'Czy jakikolwiek piksel z obrazu różnicy obrazów im3.jpg i im3.png jest nieczarny: {np.array(im3_jpg_png_roznica).any()}')

porownanie = (np.array(im3_jpg) == np.array(im3_png)).all()     # porównywanie tablic obrazów
print(
    f'Czy tablice obrazów im3.jpg i im3.png im mają te same wartości na tych samych pozycjach: {porownanie}')  # printowane jest False, zatem są różnice między obrazami w rozszerzeniach: PNG (kompresją bezstratną) a JPG (kompresją stratną)

# ppkt c.
# obrazy z zadania 1c z lab3:
obraz1_1_jpg = Image.open("obraz1_1.jpg")
obraz1_1_png = Image.open("obraz1_1.png")
obraz1_1_N_jpg = Image.open("obraz1_1N.jpg")
obraz1_1_N_png = Image.open("obraz1_1N.png")
obraz1_2_jpg = Image.open("obraz1_2.jpg")
obraz1_2_png = Image.open("obraz1_2.png")
obraz1_2_N_jpg = Image.open("obraz1_2N.jpg")
obraz1_2_N_png = Image.open("obraz1_2N.png")

plt.figure(figsize=(41.67, 31.25))

# wstawianie obrazów z rozszerzeniem JPG
plt.subplot(3, 4, 1)
plt.imshow(obraz1_1_jpg, "gray")
plt.title('obraz1_1_jpg', fontsize=30)
plt.axis("off")

plt.subplot(3, 4, 2)
plt.imshow(obraz1_1_N_jpg, "gray")
plt.title('obraz1_1_N_jpg', fontsize=30)
plt.axis("off")

plt.subplot(3, 4, 3)
plt.imshow(obraz1_2_jpg, "gray")
plt.title('obraz1_2_jpg', fontsize=30)
plt.axis("off")

plt.subplot(3, 4, 4)
plt.imshow(obraz1_2_N_jpg, "gray")
plt.title('obraz1_2_N_jpg', fontsize=30)
plt.axis("off")

# wstawianie obrazów z rozszerzeniem PNG
plt.subplot(3, 4, 5)
plt.imshow(obraz1_1_png, "gray")
plt.title('obraz1_1_png', fontsize=30)
plt.axis("off")

plt.subplot(3, 4, 6)
plt.imshow(obraz1_1_N_png, "gray")
plt.title('obraz1_1_N_png', fontsize=30)
plt.axis("off")

plt.subplot(3, 4, 7)
plt.imshow(obraz1_2_png, "gray")
plt.title('obraz1_2_png', fontsize=30)
plt.axis("off")

plt.subplot(3, 4, 8)
plt.imshow(obraz1_2_N_png, "gray")
plt.title('obraz1_2_N_png', fontsize=30)
plt.axis("off")

# wstawianie obrazów obrazujących różnice między rozszerzeniami tego samego obrazu.
plt.subplot(3, 4, 9)
plt.imshow(ImageChops.difference(obraz1_1_png, obraz1_1_jpg), "gray")
plt.title('Różnica obraz1_1_png i .jpg', fontsize=30)
plt.axis("off")

plt.subplot(3, 4, 10)
plt.imshow(ImageChops.difference(obraz1_1_N_png, obraz1_1_N_jpg), "gray")
plt.title('Różnica obraz1_1_N_png i .jpg', fontsize=30)
plt.axis("off")

plt.subplot(3, 4, 11)
plt.imshow(ImageChops.difference(obraz1_2_png, obraz1_2_jpg), "gray")
plt.title('Różnica obraz1_2_png i .jpg', fontsize=30)
plt.axis("off")

plt.subplot(3, 4, 12)
plt.imshow(ImageChops.difference(obraz1_2_N_png, obraz1_2_N_jpg), "gray")
plt.title('Różnica obraz1_2_N_png i .jpg', fontsize=30)
plt.axis("off")

plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('fig1.png')
plt.show()

obraz1_1 = ImageChops.difference(obraz1_1_png, obraz1_1_jpg)    # zapisywanie obrazów różnic tych samych obrazów o innych rozszerzeniach do zmiennych
obraz1_1_N = ImageChops.difference(obraz1_1_N_png, obraz1_1_N_jpg)
obraz1_2 = ImageChops.difference(obraz1_2_png, obraz1_2_jpg)
obraz1_2_N = ImageChops.difference(obraz1_2_N_png, obraz1_2_N_jpg)

print(f'Czy są nieczarne piksele w obrazie różnic obrazu1_1: {np.array(obraz1_1).any()}')
print(f'Czy są nieczarne piksele w obrazie różnic obraz1_1_N: {np.array(obraz1_1_N).any()}')
print(f'Czy są nieczarne piksele w obrazie różnic obraz1_2: {np.array(obraz1_2).any()}')
print(f'Czy są nieczarne piksele w obrazie różnic obraz1_2_N: {np.array(obraz1_2_N).any()}')

tab_obraz1_1_png = np.array(obraz1_1_png)
tab_obraz1_1_jpg = np.array(obraz1_1_jpg)
tab_obraz1_1_N_png = np.array(obraz1_1_N_png)
tab_obraz1_1_N_jpg = np.array(obraz1_1_N_jpg)
tab_obraz1_2_png = np.array(obraz1_2_png)
tab_obraz1_2_jpg = np.array(obraz1_2_jpg)
tab_obraz1_2_N_png = np.array(obraz1_2_N_png)
tab_obraz1_2_N_jpg = np.array(obraz1_2_N_jpg)

tab_obraz1_1_roznica = (tab_obraz1_1_png == tab_obraz1_1_jpg).all()
tab_obraz1_1_N_roznica = (tab_obraz1_1_N_png == tab_obraz1_1_N_jpg).all()
tab_obraz1_2_roznica = (tab_obraz1_2_png == tab_obraz1_2_jpg).all()
tab_obraz1_2_N_roznica = (tab_obraz1_2_N_png == tab_obraz1_2_N_jpg).all()

print(f'Czy tablice obrazów są takie same dla obraz1_1: {tab_obraz1_1_roznica}')
print(f'Czy tablice obrazów są takie same dla obraz1_1_N: {tab_obraz1_1_N_roznica}')
print(f'Czy tablice obrazów są takie same dla obraz1_2: {tab_obraz1_2_roznica}')
print(f'Czy tablice obrazów są takie same dla obraz1_2_N: {tab_obraz1_2_N_roznica}')

# Z obu porównań (ImageChops i porównanie tablic) dowiadujemy się, że istnieją różnice (niedokładności) w obrazach wytworzone przez rózne kompresje rozszerzeń tego samego obrazu.

# ----------------------------------------------------------------------------------------------------------------------------


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

# ----------------------------------------------------------------------------------------------------------------------------

# Zadanie 5
kwadrat = Image.open('kwadrat.bmp').convert('L')
kolko = Image.open('kolko.bmp').convert('L')
romb = Image.open('romb.bmp').convert('L')

# ppkt a. i b.
plt.figure(figsize=(41, 31))
plt.suptitle('Tytuły obrazów są w kolejności, w jakiej są podane jako kanały.', fontsize=60)

plt.subplot(2, 3, 1)
plt.imshow(Image.merge('RGB', (kwadrat, kolko, romb)))
plt.title('kwadrat, kolko, romb', fontsize=60)
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(Image.merge('RGB', (kwadrat, romb, kolko)))
plt.title('kwadrat, romb, kolko', fontsize=60)
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(Image.merge('RGB', (kolko, kwadrat, romb)))
plt.title('kolko, kwadrat, romb', fontsize=60)
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(Image.merge('RGB', (kolko, romb, kwadrat)))
plt.title('kolko, romb, kwadrat', fontsize=60)
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(Image.merge('RGB', (romb, kwadrat, kolko)))
plt.title('romb, kwadrat, kolko', fontsize=60)
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(Image.merge('RGB', (romb, kolko, kwadrat)))
plt.title('romb, kolko, kwadrat', fontsize=60)
plt.axis('off')

plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('fig3.png')
plt.show()
