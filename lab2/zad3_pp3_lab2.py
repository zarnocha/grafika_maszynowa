from PIL import Image  # Python Imaging Library
import numpy as np

def styk(w, h, m, n):
    # m -> szerokosc; n -> wysokosc
    tablica = np.ones((h, w), dtype=np.uint8)
    tablica[0: n, 0:m] = 0
    tablica[n:h, m:w] = 0
    return tablica * 255

# ze zdjecia z przykladu
rysunek_ramek = styk(120, 60, 50, 20)
im_ramka = Image.fromarray(rysunek_ramek)
# im_ramka.show()

rysunek_ramek = styk(120, 60, 10, 20)
im_ramka = Image.fromarray(rysunek_ramek)
im_ramka.show()

# ze zdjecia z przykladu
rysunek_ramek = styk(120, 60, 10, 40)
im_ramka = Image.fromarray(rysunek_ramek)
# im_ramka.show()