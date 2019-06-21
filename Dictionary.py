#wpsiujemy cyfry w input a program
#printuje nam ich nazwy ze słownika
phone = input("phone number: ")
slownik = {
    "1": "jeden",
    "2": "dwa",
    "3": "trzy",
    "4": "cztery"
}
output = ""
for ch in phone:
    output += slownik.get(ch, "!") + " "
print(output)
