from PIL import Image
import numpy as np
from PIL import ImageChops
import matplotlib.pyplot as plt

# LA kanał alfa dodany do obrazu L, RGBA kanał alfa dodany do obrazu RGB
shrek = Image.open("Shrek_Fiona.png")
tryby = ['1', 'L', 'LA',  'RGB','RGBA','CMYK','YCbCr','HSV',"I",'F']
plt.figure(figsize=(16, 16))
i=1
for t in tryby:
    file_name = "tryb_"+ str(t)
    im_c = shrek.convert(t)
    plt.subplot(4, 3, i)
    plt.title(str(file_name))
    plt.imshow(im_c, "gray")
    plt.axis('off')
    i +=1
plt.show()

r,g,b,a = shrek.split()
a.show()

shrek_RGB = Image.new('RGB', shrek.size, (255,255,255)) # nowy obraz wypełniony na biało
shrek_RGB.paste(shrek, (0, 0), a)
print('tryb obrazu', shrek_RGB.mode)
shrek_RGB.show()

shrek_RGB.putalpha(a)
shrek_RGB.show()

tlo = Image.open('tlo.png')
print(shrek.size, tlo.size)
tlo = tlo.resize(shrek.size, 1)
print(shrek.size, tlo.size)
tlo.show()

tlo0 = tlo.copy()
tlo0.paste(shrek, (200,300))
tlo0.show()

tlo1 = tlo.copy()
tlo1.paste(shrek, (0, 0), a) #shrek wklejony w tlo1 z maska a (kanał alpha obrazu shrek)
tlo1.show()

shrek1 = shrek.copy()
shrek1.paste(tlo, (0, 0), a) #  tlo wklejone w shrek1  z maska a
shrek1.show()


