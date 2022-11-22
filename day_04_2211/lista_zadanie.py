lista_1 = [1, 2, 3, 4, 5, 6, 88, 3, 4, 54, 33]

lista_2 = [55, 3, "Adam", 5.65, True, 4.23, "AAA"]

print(type(lista_1))
print(dir(lista_1))
# sprawdzenie, czy element jest wewnątrz listy
wynik = (89 in lista_1)
print(wynik)

"""zadanie:
zmodyfikuj kod: wczytaj od usera wartość liczbową i wypisz na ekranie indeks w liście lub info
Nie ma takiej danej gdy nie znajdziesz tego w liście
"""
flag = True
while flag:
    number = int(input('Wpisz liczbę: '))
    if number in lista_1:
        print(f'Szukana wartość {number} znajduje się na pozycji {lista_1.index(number)} w liście.')
        flag = False
    else:
        print("Nie ma takiego numberu w liście.")
