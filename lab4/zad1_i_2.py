import numpy as np
from PIL import Image, ImageChops

# Zadanie 1
im1 = Image.open('obraz.jpg')


# Zadanie 2
# ppkt a.
tablica_obrazu = np.array(im1)

# kanały R, G, B
t_r = tablica_obrazu[:, :, 0]
t_g = tablica_obrazu[:, :, 1]
t_b = tablica_obrazu[:, :, 2]

# obrazy z kanałów R, G, B
im_r = Image.fromarray(t_r)
im_g = Image.fromarray(t_g)
im_b = Image.fromarray(t_b)

im_r.save('im_r.jpg')
im_g.save('im_g.jpg')
im_b.save('im_b.jpg')

# ppkt b.
im2 = Image.merge('RGB', (im_r, im_g, im_b))
im1_2_roznica = ImageChops.difference(im1, im2)  # wniosek: obrazy są takie same, bo obraz powstały z różnic jest cały czarny
im1_2_roznica.show()
print(f'Czy jakikolwiek piksel z obrazu różnicy obrazów jest nieczarny: {np.array(im1_2_roznica).any()}')

# ppkt c.
porownanie = (np.array(im2) == np.array(im1)).all()
print(f'Czy tablice obrazów im2 i im1 mają te same wartości na tych samych pozycjach: {porownanie}')  # printowane jest True, zatem obraz nie ma żadnych różnic w pikselach.
