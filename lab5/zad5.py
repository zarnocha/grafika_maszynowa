import numpy as np
from PIL import Image

obraz = Image.open('obraz.jpg')

T = np.array(obraz, dtype='uint8')
T += 100

obraz_wynik = Image.fromarray(T, "RGB")
obraz_wynik.show()
obraz_wynik.save('Zadanie5_tablica.jpg')

obraz_wynik = obraz.point(lambda i: i + 100)
obraz_wynik.show()
obraz_wynik.save('Zadanie5_point.jpg')

