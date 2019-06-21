waga = int(input('Twoja waga: '))
konwersja = input('Lbs wpisz "L", Kg wpisz "K": ')

if konwersja.upper() == "L":
    waga_LBS = waga * 0.45
    print(f"Twoja waga to {waga_LBS} kg")


elif konwersja.upper() == "K":
    waga_kg = waga / 0.45
    print(f'Twoja waga to {waga_kg} pounds')


else:
    konwersja.upper() != "L" or "K"
    print("Błąd edycji! Wprowadź 'K' lub 'L'")


# print(f'Twoja waga to {waga_kg} lbs')
# f <---- jest potrzebne do tego żeby waga_kg wyświetliła
# się jako wartość a nie jako ciąg znaków
# dzięki int w pierwszej lini możemy mnożyć przez liczby nie całkowite
