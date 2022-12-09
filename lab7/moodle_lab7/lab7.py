from PIL import Image
from PIL import ImageFilter
from PIL import ImageChops



im = Image.open('lab7/baby_yoda.jpg')
print("tryb obrazu", im.mode)
print("rozmiar", im.size)

#  Class   PIL.ImageFilter.Kernel(size, kernel, scale=None, offset=0) -- scale jest zazwyczaj sumą wyrazów w kernel, w algorytmie kernel normalizujemy dzieląc przez scale
fe = im.filter(ImageFilter.FIND_EDGES) # filtruje obraz im
fe.show()
print(ImageFilter.FIND_EDGES.filterargs)  # wyświetla argumenty, w tym rozmiar i  wartości tablicy Kernel

ImageFilter.FIND_EDGES.filterargs = ((3, 3), 1, 0, (-1, -1, -1, -1, 6, -1, -1, -1, -1)) # pozwala zmieniac wartości listy Kernel, skalę i offset.
fe1 = im.filter(ImageFilter.FIND_EDGES) # filtruje obraz im
fe1.show()

ImageFilter.FIND_EDGES.filterargs = ((3, 3), 1, 0, (-1, -1, -1, -1, 8, -1, -1, -1, -1)) # pozwala zmieniac wartości listy Kernel, skalę i offset.
fe3 = im.filter(ImageFilter.FIND_EDGES) # filtruje obraz im
fe3.show()
fe_ker = im.filter(ImageFilter.Kernel(size = (3, 3), kernel = (-1, -1, -1, -1, 8, -1, -1, -1, -1), scale=1, offset=0))
fe_ker.show()
roznica = ImageChops.difference(fe3, fe_ker)
roznica.show()


