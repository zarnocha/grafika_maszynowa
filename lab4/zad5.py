from PIL import Image
from matplotlib import pyplot as plt

# Zadanie 5
kwadrat = Image.open('kwadrat.bmp').convert('L')
kolko = Image.open('kolko.bmp').convert('L')
romb = Image.open('romb.bmp').convert('L')

# ppkt a. i b.
plt.figure(figsize=(41, 31))
plt.suptitle('Tytuły obrazów są w kolejności, w jakiej są podane jako kanały.', fontsize=60)

plt.subplot(2, 3, 1)
plt.imshow(Image.merge('RGB', (kwadrat, kolko, romb)))
plt.title('kwadrat, kolko, romb', fontsize=60)
plt.axis('off')

plt.subplot(2, 3, 2)
plt.imshow(Image.merge('RGB', (kwadrat, romb, kolko)))
plt.title('kwadrat, romb, kolko', fontsize=60)
plt.axis('off')

plt.subplot(2, 3, 3)
plt.imshow(Image.merge('RGB', (kolko, kwadrat, romb)))
plt.title('kolko, kwadrat, romb', fontsize=60)
plt.axis('off')

plt.subplot(2, 3, 4)
plt.imshow(Image.merge('RGB', (kolko, romb, kwadrat)))
plt.title('kolko, romb, kwadrat', fontsize=60)
plt.axis('off')

plt.subplot(2, 3, 5)
plt.imshow(Image.merge('RGB', (romb, kwadrat, kolko)))
plt.title('romb, kwadrat, kolko', fontsize=60)
plt.axis('off')

plt.subplot(2, 3, 6)
plt.imshow(Image.merge('RGB', (romb, kolko, kwadrat)))
plt.title('romb, kolko, kwadrat', fontsize=60)
plt.axis('off')

plt.subplots_adjust(wspace=0.1, hspace=0.1)
plt.savefig('fig3.png')
plt.show()
