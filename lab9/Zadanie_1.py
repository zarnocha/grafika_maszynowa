# from PIL import Image
# import numpy as np
# from PIL import ImageChops
# import matplotlib.pyplot as plt
# from PIL import ImageStat as stat
#
# obraz1 = Image.open('obraz1.png')
# obraz3 = Image.new('RGB', obraz1.size, (255,255,255))
# r, g, b, a = obraz1.split()
# obraz3.paste(obraz1, (0, 0), a)
#
# tryby =  ['CMYK','YCbCr','HSV']
# obraz3_CMYK = obraz3.convert("CMYK")
# obraz3_YCbCr = obraz3.convert("YCbCr")
# obraz3_HSV = obraz3.convert("HSV")
#
# plt.subplot(1, 3, 1)
# plt.imshow(ImageChops.difference(obraz3_CMYK, obraz3_YCbCr))
# plt.axis('off')
#
# plt.subplot(1, 3, 2)
# plt.imshow(ImageChops.difference(obraz3_CMYK, obraz3_HSV))
# plt.axis('off')
#
# plt.subplot(1, 3, 3)
# plt.imshow(ImageChops.difference(obraz3_YCbCr, obraz3_HSV))
# plt.axis('off')
#
# plt.tight_layout()
# plt.show()
# plt.savefig('ycbcr.png')

######################################33

from PIL import Image
import numpy as np

obraz1 = Image.open('test.png')
obraz1 = obraz1.convert('HSV')
h, s, v = obraz1.split()

# obraz3.paste(obraz1, (0, 0), a)
# r.show()
# obraz3 = Image.new('HSV', obraz1.size, (360, 0, 255))
# obraz3 = obraz3.convert('HSV')
# tmp = np.asarray(obraz3)
# tmp = tmp.copy()
# obraz3 = Image.fromarray(tmp, mode='HSV')
obraz1.resize()