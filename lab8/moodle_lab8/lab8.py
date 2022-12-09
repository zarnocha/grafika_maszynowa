from PIL import Image
import numpy as np
from PIL import ImageChops, ImageOps, ImageShow
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


def statystyki(im):
    s = stat.Stat(im)
    print("extrema ", s.extrema)  # max i min
    print("count ", s.count)  # zlicza
    print("mean ", s.mean)  # srednia
    print("median ", s.median)  # mediana
    print("stddev ", s.stddev)  # odchylenie standardowe


#************************************************************************************************************
im = Image.open('brain.png')
print(im.mode)
statystyki(im)

plt.title("brain oryginalny ")
plt.axis('off')
plt.imshow(im, 'gray')
plt.show()

szary = im.convert("L")
statystyki(szary)
#print(szary.histogram())

im_equalized1 = ImageOps.equalize(szary, mask=None) # https://pillow.readthedocs.io/en/stable/reference/ImageOps.html
plt.title("brain wyrównany ")
plt.axis('off')
plt.imshow(im_equalized1, 'gray')
plt.show()
statystyki(im_equalized1)



#________________________________________________________________

im = Image.open('mgla.jpg') # obraz kolorowy

im.show()

statystyki(im)
hist = im.histogram()
plt.title("histogram - mgła ")
plt.bar(range(256), hist[:256], color='r', alpha=0.5)
plt.bar(range(256), hist[256:2 * 256], color='g', alpha=0.4)
plt.bar(range(256), hist[2 * 256:], color='b', alpha=0.3)
plt.show()

r, g, b = im.split()
# wyrównanie każdego kanału oddzielnie
r_eq = ImageOps.equalize(r)
g_eq = ImageOps.equalize(g)
b_eq = ImageOps.equalize(b)
im1 = Image.merge('RGB', (r_eq, g_eq, b_eq))
im1.show()

# wyrównaie obrazu RGB
im_equalized1 = ImageOps.equalize(im, mask=None)
im_equalized1.show()

#porównanie
diff=ImageChops.difference(im_equalized1, im1)
print("statystyki róznicy -------------------------------")
statystyki(diff)

# konwersja na szary i wyrównanie
im3 = im.convert("L")
im3.show()
im3_eq = ImageOps.equalize(im3)
im3_eq.show()

