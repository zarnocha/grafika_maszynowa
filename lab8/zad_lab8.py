from PIL import Image, ImageOps, ImageFilter, ImageChops
from PIL import ImageStat as stat
import matplotlib.pyplot as plt


# Zadanie 1:
im = Image.open('obraz.jpg')
print('Przed przekonwertowaniem:', im.mode)

im = im.convert('L')
print('Po przekonwertowaniu:', im.mode, end='\n\n')


# Zadanie 2:
def statystyki(im):
    s = stat.Stat(im)
    print("Min. i max. wartości obrazu:", s.extrema)
    print("Ilość pikseli obrazu:", s.count)
    print("Średni poziom pikseli obrazu:", s.mean)
    print("Mediana poziomu pikseli obrazu:", s.median)
    print("Odchylenie std pikseli obrazu:", s.stddev)


print('Statystyki obrazu:')
statystyki(im)


# Zadanie 3:
def histogram_norm(obraz):
    histogram = obraz.histogram()
    s = stat.Stat(obraz)
    ilosc = s.count[0]
    histogram_znormalizowany = [wartosc / ilosc for wartosc in histogram]
    return histogram_znormalizowany


plt.plot(im.histogram())
plt.grid()
plt.tight_layout()
plt.savefig('histogram_obrazu.png')
plt.show()


histogram_znormalizowany = histogram_norm(im)
plt.plot(histogram_znormalizowany)

lista_procentow_string = []
lista_procentow = []
for i in range(1, len(plt.yticks()[0])):
    lista_procentow.append(round(plt.yticks()[0][i], 3))
    lista_procentow_string.append(f'{round(plt.yticks()[0][i], 3) * 1000}%')

plt.yticks(lista_procentow, lista_procentow_string)
plt.grid()
plt.tight_layout()
plt.savefig('histogram_znormalizowany.png')
plt.show()


# Zadanie 4:
def histogram_cumul(obraz):
    histogram_zmormalizowany = histogram_norm(obraz)
    histogram_skumulowany = [histogram_zmormalizowany[0]]
    for i in range(1, len(histogram_zmormalizowany)):
        histogram_skumulowany.append(histogram_skumulowany[i - 1] + histogram_zmormalizowany[i])

    return histogram_skumulowany


lista_procentow_string = []
lista_procentow = []
for i in range(0, 11, 2):
    lista_procentow.append(i / 10)
    lista_procentow_string.append(f'{i * 10}%')

histogram_skumulowany = histogram_cumul(im)

plt.plot(histogram_skumulowany)
plt.yticks(ticks=lista_procentow, labels=lista_procentow_string)
plt.tight_layout()
plt.grid()
plt.savefig('histogram_skumulowany.png')
plt.show()


# Zadanie 5:
def histogram_equalization(obraz):
    histogram_skumulowany = histogram_cumul(obraz)
    obraz_wyrownany = im.point(lambda p: int(255 * histogram_skumulowany[p]))
    return obraz_wyrownany


histogram_equalization(im).save('equalized.png')
plt.plot(histogram_equalization(im).histogram())
plt.plot(im.histogram())
plt.legend(['Histogram wyrównany', 'Histogram niewyrównany'])
plt.tight_layout()
plt.savefig('histogram_wyrownany_i_niewyrownany.png')
plt.show()

plt.figure()
plt.subplot(1, 2, 1)
plt.title('obraz.jpg')
plt.imshow(im, 'gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Ten sam obraz\nz wyrównanym histogramem')
plt.imshow(histogram_equalization(im), 'gray')

plt.axis('off')
plt.tight_layout()
plt.savefig('obraz_i_histogram_wyrownany.png')
plt.show()


# Zadanie 6:
ImageOps.equalize(im).save('equalized1.png')


# ppkt 6.1
plt.figure()
plt.subplot(1, 2, 1)
plt.title('equalized.png')
plt.imshow(histogram_equalization(im), 'gray')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('equalized1.png')
plt.imshow(ImageOps.equalize(im), 'gray')

plt.axis('off')
plt.tight_layout()
plt.savefig('porownanie_obrazow_histogramow.png')
plt.show()

ImageChops.difference(histogram_equalization(im), ImageOps.equalize(im)).save('roznica_w_obrazach.png')


# ppkt 6.2
plt.figure()
plt.subplot(1, 2, 1)
plt.title('Własna funkcja\nwyrównująca histogram')
plt.plot(histogram_equalization(im).histogram())
plt.grid()

plt.subplot(1, 2, 2)
plt.title('ImageOps.equalize(im)')
plt.plot(ImageOps.equalize(im).histogram())
plt.grid()

plt.tight_layout()
plt.savefig('porownanie_histogramow.png')
plt.show()


# ppkt 6.3
print('\nStatystyki histogram_equalization(im):')
statystyki(histogram_equalization(im))

print('\nStatystyki ImageOps.equalize(im):')
statystyki(ImageOps.equalize(im))


# Zadanie 7:
DETAIL = im.filter(ImageFilter.DETAIL)
SHARPEN = im.filter(ImageFilter.SHARPEN)
CONTOUR = im.filter(ImageFilter.CONTOUR)

plt.figure()

plt.subplot(2, 2, 1)
plt.imshow(DETAIL, 'gray')
plt.title("DETAIL filter")
plt.axis('off')

plt.subplot(2, 2, 2)
plt.imshow(SHARPEN, 'gray')
plt.title("SHARPEN filter")
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(CONTOUR, 'gray')
plt.title("CONTOUR filter")
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(ImageOps.equalize(im), 'gray')
plt.title("equalized1.png")
plt.axis('off')

plt.tight_layout()
plt.savefig('filtry.png')
plt.show()
