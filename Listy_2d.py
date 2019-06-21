#usuwanie duplikatów cyfr z listy.
#print zwraca pojedyńcze cyfry bez duplikowania
numbers = [4, 5, 8, 9, 2, 9, 5]
unix = []
for number in numbers:
    if number not in unix:
        unix.append(number)
print(unix)
#------------------------------------------------#
#przypisywanie wartości z listy do zmiennych
#proste rozwiązanie
numbers = (1, 2, 3)
x, y, z = numbers
print(x)