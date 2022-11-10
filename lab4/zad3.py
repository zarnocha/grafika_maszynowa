import numpy as np
from PIL import Image, ImageChops
import matplotlib.pyplot as plt

# ppkt a.

im1 = Image.open('obraz.jpg')

r, g, b = im1.split()

im3 = Image.merge('RGB', (b, r, g))
im3.save('im3.jpg')
im3.save('im3.png')

# ppkt b.
im3_1 = Image.open('im3.jpg')
im3_2 = Image.open('im3.png')

ImageChops.difference(im3_1, im3_2).show()
porownanie = np.array(im3_1) == np.array(im3_2)
porownanie = porownanie.all()
print(porownanie)   # printowane jest False, zatem są różnice między PNG (kompresją bezstratną) a JPG (kompresją stratną)

# ppkt c.
obraz1_1_jpg = Image.open("lab3_zad1c/obraz1_1.jpg")
obraz1_1_png = Image.open("lab3_zad1c/obraz1_1.png")
obraz1_1_N_jpg = Image.open("lab3_zad1c/obraz1_1N.jpg")
obraz1_1_N_png = Image.open("lab3_zad1c/obraz1_1N.png")
obraz1_2_jpg = Image.open("lab3_zad1c/obraz1_2.jpg")
obraz1_2_png = Image.open("lab3_zad1c/obraz1_2.png")
obraz1_2_N_jpg = Image.open("lab3_zad1c/obraz1_2N.jpg")
obraz1_2_N_png = Image.open("lab3_zad1c/obraz1_2N.png")

plt.figure(figsize=(41.67, 31.25))

# .JPG

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

# .PNG

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

# różnice

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

obraz1_1 = ImageChops.difference(obraz1_1_png, obraz1_1_jpg)
obraz1_1_N = ImageChops.difference(obraz1_1_N_png, obraz1_1_N_jpg)
obraz1_2 = ImageChops.difference(obraz1_2_png, obraz1_2_jpg)
obraz1_2_N = ImageChops.difference(obraz1_2_N_png, obraz1_2_N_jpg)

obraz1_1_roznica = obraz1_1 == obraz1_1_N
obraz1_2_roznica = obraz1_2 == obraz1_2_N
print(f'Róznica ImageChops dla obraz1_1: {obraz1_1_roznica}')
print(f'Róznica ImageChops dla obraz1_2: {obraz1_2_roznica}')

tab_obraz1_1 = np.array(obraz1_1)
tab_obraz1_1_N = np.array(obraz1_1_N)
tab_obraz1_2 = np.array(obraz1_2)
tab_obraz1_2_N = np.array(obraz1_2_N)

tab_obraz1_1_roznica = tab_obraz1_1 == tab_obraz1_1_N
tab_obraz1_2_roznica = tab_obraz1_2 == tab_obraz1_2_N

print(f'Róznica w tablicach obraz1_1: {tab_obraz1_1_roznica.all()}')
print(f'Róznica w tablicach obraz1_2: {tab_obraz1_2_roznica.all()}')

# Z obu porównań dowiadujemy się, że istnieją różnice w rozszerzeniach przy tym samym obrazie.
