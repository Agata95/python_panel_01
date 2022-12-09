import dumper

zmienna_slownik_0 = {
    'name': 'Jurkiewicz Adam',
    'age': 48,
    'email': 'adam@jurkiewicz.tech',
}

zmienna_slownik_1 = {
    'name': 'Jurkiewicz Adam',
    'age': 48,
    'email': 'adam@jurkiewicz.tech',
    'cosik': [2, 3, 55],
}

zmienna_slownik_2 = {
    'name': 'Adam Jurkiewicz',
    'age': 48,
    'adress': 'Warszawa',
    'mail': 'adam@jurkiewicz.tech',
    'web': 'https://python.szkola.pl',
    'os': 'Linux',
    'adress1': 'Warszawa',
}

print(zmienna_slownik_0)
print(zmienna_slownik_1)
print(zmienna_slownik_2)

print(type(zmienna_slownik_0))
print(type(zmienna_slownik_1))
print(type(zmienna_slownik_2))

dumper.dump(zmienna_slownik_0)
print()
dumper.dump(zmienna_slownik_1)
print()
dumper.dump(zmienna_slownik_2)