from PIL import Image
import numpy as np

# Zadanie 2:
obraz = Image.open("inicjaly.bmp")  # Otwieramy obraz z rozszerzeniem .bmp
print("tryb:", obraz.mode)
print("format:", obraz.format)
print("rozmiar:", obraz.size)

# Zadanie 3:
dane_obrazu = np.asarray(obraz)  # Wczytujemy wczesniej otwarty obraz jako tablice (bool'ow)
dane_obrazu = dane_obrazu * 1  # Zamieniamy tablice bool'ow na tablice int'ow

tablica_do_pliku = open('inicjaly.txt', 'w')  # Zapisujemy tablice ze zmiennej dane_obrazu do pliku inicjaly.txt
for wiersze in dane_obrazu:
    for piksel in wiersze:
        tablica_do_pliku.write(str(piksel) + ' ')
    tablica_do_pliku.write('\n')

# Zadanie 4:
#   a.
t = np.loadtxt("inicjaly.txt")  # Wczytujemy wczesniej utworzony plik .txt do zmiennej t; jeśli błąd: należy zakomentować linie od 14 do 18

print("\n" + "typ danych tablicy t:", t.dtype)  # typ danych w zmiennej t
print("rozmiar tablicy t:", t.shape)  # rozmiar tablicy t
x, y = t.shape  # przypisanie wymiarow tablicy do zmiennych x i y
print("ilosc elementow tablicy t:", x*y)  # rozmiar tablicy  (można zastępczo użyć t.size)
print("wymiar tablicy t:", t.ndim)

#   b.
# Dowolnie wybrany punkt:
print('\n(67, 5):', str(t[5][67]))  # (67, 5) w paincie => t[5][67]

# Wartosci z pikseli o adresach (50, 30), (90, 40), (99,0):
print('(50, 30):', str(t[30][50]))  # (50, 30) w paincie => t[30][50]
print('(90, 40):', str(t[40][90]))  # (90, 40) w paincie => t[40][90]
print('(99, 0):', str(t[0][99]))  # (99,0) w paincie => t[0][99]

# Zadanie 5:
#   Porownanie tablic t oraz t_bool
t_bool = np.loadtxt("inicjaly.txt", dtype=np.bool_)
porowanie_tablic = t == t_bool
print("\n" + "Porownanie tablic t oraz t_bool:", porowanie_tablic.all())

#   Porownanie informacji tablic t oraz t_bool
informacje_t = [t.dtype, t.shape, t.ndim]
informacje_t_bool = [t_bool.dtype, t_bool.shape, t_bool.ndim]
porowanie_informacji = informacje_t == informacje_t_bool

print("Porownanie informacji:", porowanie_informacji)

# Zadanie 6:
#   Porownanie tablic t oraz t_int
t_int = np.loadtxt("inicjaly.txt", dtype=np.int_)
porowanie_tablic = t == t_int
print("\n" + "Porownanie tablic t oraz t_int:", porowanie_tablic.all())

#   Porownanie informacji tablic t oraz t_int
informacje_t_int = [t_int.dtype, t_int.shape, t_int.ndim]
porowanie_informacji = informacje_t == informacje_t_int
print("Porownanie informacji:", porowanie_informacji)

#   a.
obraz_t_int = Image.fromarray(t_int)
obraz_t_int.show()
obraz_t_int.save('obraz_t_int.bmp')
