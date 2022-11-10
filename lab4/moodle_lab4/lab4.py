from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt


im = Image.open('jesien.jpg')
print("tryb", im.mode)
print("format", im.format)
print("rozmiar", im.size)
h, w = im.size
im.show()

# tablica obrazu
T = np.array(im)
#tablica kanału r
t_r = T[:, :, 0]
im_r = Image.fromarray(t_r) # obraz w odcieniuach szarości kanału r
print("tryb", im_r.mode)
#tablica kanału g
t_g = T[:, :, 1]
im_g = Image.fromarray(t_g) # obraz w odcieniuach szarości kanału g
print("tryb", im_g.mode)
#tablica kanału b
t_b = T[:, :, 2]
im_b = Image.fromarray(t_b) # obraz w odcieniuach szarości kanału b
print("tryb", im_b.mode)


# przedstawienie 4 obrazów w jednym oknie plt
plt.figure(figsize=(32, 16))
plt.subplot(2,2,1) # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im)
plt.axis('off')
plt.subplot(2,2,2)
plt.imshow(im_r, "gray")
plt.axis('off')
plt.subplot(2,2,3)
plt.imshow(im_g, "gray")
plt.axis('off')
plt.subplot(2,2,4)
plt.imshow(im_b, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.savefig('lab4/figura1.png')
plt.show()      # najpierw zapisać a potem wyświetlić, bo wyświetlenie czyści obrazek.



# Kanały pobrane jako obrazy
r, g, b = im.split()  # powstają obrazy
print("tryb", r.mode)
print("tryb", g.mode)
print("tryb", b.mode)
diff_r = ImageChops.difference(r, im_r)     # porównywanie tych z tablicy
diff_g = ImageChops.difference(g, im_g)
diff_b = ImageChops.difference(b, im_b)


plt.figure(figsize=(32, 16))
plt.subplot(3, 4, 1)  # ile obrazów w pionie, ile w poziomie, numer obrazu
plt.imshow(im)
plt.axis('off')

plt.subplot(3, 4, 2)
plt.imshow(im_r, "gray")    # trzeba wymusić pokazywanie szarych kanałów
plt.axis('off')

plt.subplot(3,4,3)
plt.imshow(im_g, "gray")
plt.axis('off')

plt.subplot(3,4,4)
plt.imshow(im_b, "gray")
plt.axis('off')
plt.subplot(3,4,5)
plt.imshow(im)
plt.axis('off')
plt.subplot(3,4,6)
plt.imshow(r, "gray")
plt.axis('off')
plt.subplot(3,4,7)
plt.imshow(g, "gray")
plt.axis('off')
plt.subplot(3,4,8)
plt.imshow(b, "gray")
plt.axis('off')
plt.subplot(3,4,9)
plt.imshow(im)
plt.axis('off')
plt.subplot(3,4,10)
plt.imshow(diff_r, "gray")
plt.axis('off')
plt.subplot(3,4,11)
plt.imshow(diff_g, "gray")
plt.axis('off')
plt.subplot(3,4,12)
plt.imshow(diff_b, "gray")
plt.axis('off')
plt.subplots_adjust(wspace=0.05, hspace=0.05)
plt.show()

# zapis kanałów do tablic
r_T = np.array(r)
g_T = np.array(g)
b_T = np.array(b)

# porównanie tablic
print("--------porównanie tablic--------------")
porownanie = r_T == t_r
czy_rowne = porownanie.all()
print(czy_rowne)
print("----------------------")



im1 = Image.merge('RGB', (im_r, im_g, im_b))
im2 = Image.merge('RGB', (r, g, b)) # zamień r na im_r i sprawdź efekt
# im1.show()
# im2.show()
diff_im = ImageChops.difference(im1,im2)
diff_im.show()

# mieszanie kanałow
im3 = Image.merge('RGB', (r, b, g))
im3.show()



# konwersja na  obraz w odcieniach szarości
w1 = 0.3
w2 = 0.8
w3 = 0.2
szary = w1 * r_T + w2 * g_T + w3 * b_T
szary_im = Image.fromarray(szary)
szary_im.show()


# własna tablica "L" jako kanał
t = (w, h)
A = np.zeros(t, dtype=np.uint8)
A_im = Image.fromarray(A)

im4 = Image.merge('RGB', (r, A_im, b))
im4.show()


# własna tablica "L" jako kanał - drugi przykład
B = np.ones(t, dtype=np.uint8)
for i in range(w):
    for j in range(h):
        B[i, j] = (i + j) % 256

B_im = Image.fromarray(B)
B_im.show()
im6 = Image.merge('RGB', (B_im, g, b))
im6.show()



