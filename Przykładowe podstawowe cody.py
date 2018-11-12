marka = 'Peguet'
ilosc_drzwi = 5
pojemnosc = 1.3

marka_up = marka.upper()  # funcja zmienia wielkosc liter na małe - marka.upper zmienia na duze

print('Samochod ' + (marka_up) + ' ma ' + str(ilosc_drzwi) + " drzwi")

print("Pojemnosc po zmianach: " + str(pojemnosc * 2))

print(marka_up)

# OTWIERANIE I ODCZYTYWANIE PLIKOW, OPEN, READ, WRITE
# r - tylko odczyt pliku, jeśli plik nie istnieje to wywala blad
# r+ - oczyt i edycja pliku
# w  - edycja, twozenie nowego jesli nie istnieje i kasowanie zapisanych danych
# w+ - wszystko  + kursor na poczatku
# a - edycja i twozenie nowego pliku
# a+ - wszystko oprucz kasowania danych, kursor ustawia się na koncu
########################################
f = open("plik.txt", "r")
print(f.readlines())
f.close()
# f.read - oczyt, f.write - zapis f.readlines - odczyt wybranych lini
# adres filmu - https://www.youtube.com/watch?v=fwMyIL6LRA8&list=PLdBHMlEKo8UcOaykMssI1_X6ui0tzTNoH&index=15
#######################################

