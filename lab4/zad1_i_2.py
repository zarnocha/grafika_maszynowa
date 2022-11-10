import numpy as np
from PIL import Image, ImageChops

# Zadanie 1
im1 = Image.open('obraz.jpg')


# Zadanie 2

# kanały R, G, B
T = np.array(im1)
t_r = T[:, :, 0]
t_g = T[:, :, 1]
t_b = T[:, :, 2]

# obrazy z kanałów R, G, B
im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)

im2 = Image.merge('RGB', (im_r, im_g, im_b))
ImageChops.difference(im1, im2).show()  # wniosek: obrazy są takie same, bo tablica różnic jest cała czarna

porownanie = np.array(im2) == np.array(im1)
porownanie = porownanie.all()
print(porownanie)  # printowane jest True, zatem obraz nie ma żadnych różnic w pikselach.
