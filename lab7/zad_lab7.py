import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageFilter, ImageChops

im = Image.open('obraz.jpg')


# Zadanie 1:
def zakres(w, h):
    return [(i, j) for i in range(w) for j in range(h)]


def filtruj(obraz, kernel, scale):
    w, h = obraz.size
    pixele_obraz = obraz.load()
    kopia = obraz.copy()
    pixele_kopia = kopia.load()

    for i in range((int(len(kernel) / 2)), w - int(len(kernel) / 2)):
        for j in range(int(len(kernel) / 2), h - int(len(kernel) / 2)):
            tmp_arr = np.zeros(np.array(kernel).shape, dtype=object)
            for x, y in zakres(len(kernel), len(kernel)):
                a = i + x - int(len(kernel) / 2)
                b = j + y - int(len(kernel) / 2)

                tmp_arr[x, y] = (pixele_obraz[a, b] * kernel[x][y])

                if len(tmp_arr[x][y]) == 0:
                    tmp_arr[x][y] = tuple(np.zeros(3, dtype=int))

            suma = [0, 0, 0]
            for x, y in zakres(len(kernel), len(kernel)):
                for rgb in range(0, 3):
                    suma[rgb] += int(tmp_arr[x][y][rgb])

            pixele_kopia[i, j] = (int(suma[0] / scale), int(suma[1] / scale), int(suma[2] / scale))

    return kopia


# Zadanie 2:
parametry_BLUR = ImageFilter.BLUR.filterargs
kernel_BLUR = [
    [1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1]
    ]
# ppkt a.
blur = filtruj(im, kernel_BLUR, parametry_BLUR[1])
blur1 = im.filter(ImageFilter.BLUR)

# ppkt b.
plt.figure(figsize=(15, 18))
plt.subplot(1, 3, 1)
plt.imshow(blur)
plt.title('Moja f-cja BLUR')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(blur1)
plt.title('F-cja Image.filter() z BLUR')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(ImageChops.difference(blur, blur1))
plt.title('Róznica w filtrach')
plt.axis('off')

plt.subplots_adjust(wspace=0.9)
plt.savefig('fig1.png')


# Zadanie 3:
# ppkt a.
im_l = im.convert('L')
SOBEL1 = ImageFilter.EMBOSS
SOBEL1.filterargs = ((3, 3), 1, 128, (-1,  0,  1, -2,  0,  2, -1,  0,  1))
sobel1 = im.filter(SOBEL1)

# ppkt b.
SOBEL2 = ImageFilter.EMBOSS
SOBEL2.filterargs = ((3, 3), 1, 128, (-1, -2, -1, 0,  0, 0, 1, 2, 1))
sobel2 = im.filter(SOBEL2)

# ppkt c.
plt.figure(figsize=(15, 18))
plt.subplot(1, 3, 1)
plt.imshow(im_l, 'gray')
plt.title('Obraz\nkonwertowany\nna L')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(sobel1, 'gray')
plt.title('F-cja SOBEL 1')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(sobel2, 'gray')
plt.title('F-cja SOBEL 2')
plt.axis('off')

plt.subplots_adjust(wspace=0.9)
plt.savefig('fig2.png')


# Zadanie 4:
# ppkt. 0
plt.figure(figsize=(15, 18))

plt.subplot(4, 2, 1)
plt.imshow(im.filter(ImageFilter.DETAIL()))
plt.title("DETAIL", wrap=True)
plt.axis('off')

plt.subplot(4, 2, 2)
plt.imshow(ImageChops.difference(im, im.filter(ImageFilter.DETAIL())))
plt.title("Róznica w obrazie i DETAIL", wrap=True)
plt.axis('off')

plt.subplot(4, 2, 3)
plt.imshow(im.filter(ImageFilter.EDGE_ENHANCE_MORE()))
plt.title("EDGE_ENHANCE_MORE", wrap=True)
plt.axis('off')

plt.subplot(4, 2, 4)
plt.imshow(ImageChops.difference(im, im.filter(ImageFilter.EDGE_ENHANCE_MORE())))
plt.title("Różnica w obrazie i\nEDGE_ENHANCE_MORE", wrap=True)
plt.axis('off')

plt.subplot(4, 2, 5)
plt.imshow(im.filter(ImageFilter.SHARPEN()))
plt.title("SHARPEN", wrap=True)
plt.axis('off')

plt.subplot(4, 2, 6)
plt.imshow(ImageChops.difference(im, im.filter(ImageFilter.SHARPEN())))
plt.title("Różnica w obrazie i SHARPEN", wrap=True)
plt.axis('off')

plt.subplot(4, 2, 7)
plt.imshow(im.filter(ImageFilter.SMOOTH_MORE()))
plt.title("SMOOTH_MORE", wrap=True)
plt.axis('off')

plt.subplot(4, 2, 8)
plt.imshow(ImageChops.difference(im, im.filter(ImageFilter.SMOOTH_MORE())))
plt.title("Różnica w obrazie i\nSMOOTH_MORE", wrap=True)
plt.axis('off')

plt.subplots_adjust(wspace=0.4, hspace=0.9)
plt.savefig('fig3.png')

# ppkt b.
plt.figure(figsize=(15, 18))

plt.subplot(5, 2, 1)
plt.imshow(im.filter(ImageFilter.GaussianBlur(radius=5)))
plt.title("GaussianBlur(radius=5)", wrap=True)
plt.axis('off')

plt.subplot(5, 2, 2)
plt.imshow(ImageChops.difference(im, im.filter(ImageFilter.GaussianBlur(radius=5))))
plt.title("Różnica w obrazie i GaussianBlur", wrap=True)
plt.axis('off')

plt.subplot(5, 2, 3)
plt.imshow(im.filter(ImageFilter.UnsharpMask(radius=5, percent=150, threshold=2)))
plt.title("UnsharpMask(radius=5, percent=150, threshold=2)", wrap=True)
plt.axis('off')

plt.subplot(5, 2, 4)
plt.imshow(ImageChops.difference(im, im.filter(ImageFilter.UnsharpMask(radius=5, percent=150, threshold=2))))
plt.title("Różnica w obrazie i UnsharpMask", wrap=True)
plt.axis('off')

plt.subplot(5, 2, 5)
plt.imshow(im.filter(ImageFilter.MedianFilter(size=5)))
plt.title("MedianFilter(size=5)", wrap=True)
plt.axis('off')

plt.subplot(5, 2, 6)
plt.imshow(ImageChops.difference(im, im.filter(ImageFilter.MedianFilter(size=5))))
plt.title("Różnica w obrazie i MedianFilter", wrap=True)
plt.axis('off')

plt.subplot(5, 2, 7)
plt.imshow(im.filter(ImageFilter.MinFilter(size=5)))
plt.title("MinFilter(size=3)", wrap=True)
plt.axis('off')

plt.subplot(5, 2, 8)
plt.imshow(ImageChops.difference(im, im.filter(ImageFilter.MinFilter(size=5))))
plt.title("Różnica w obrazie i MinFilter", wrap=True)
plt.axis('off')

plt.subplot(5, 2, 9)
plt.imshow(im.filter(ImageFilter.MaxFilter(size=5)))
plt.title("MaxFilter(size=5)", wrap=True)
plt.axis('off')

plt.subplot(5, 2, 10)
plt.imshow(ImageChops.difference(im, im.filter(ImageFilter.MaxFilter(size=5))))
plt.title("Różnica w obrazie i MaxFilter", wrap=True)
plt.axis('off')

plt.subplots_adjust(wspace=0.3, hspace=0.6)
plt.savefig('fig4.png')
