# https://docs.python.org/3/library/json.html
import json

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

print(json.dumps(zmienna_slownik_0, indent=4))
print(zmienna_slownik_1)
print(zmienna_slownik_2)
print(json.dumps(zmienna_slownik_2, indent=2))