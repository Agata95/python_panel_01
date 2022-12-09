import csv
from faker import Faker
from random import random


def i(n=10000):
    return int(random() * n)


dane = Faker("pl_PL")


with open("dane_testowe.csv", mode='w', encoding="windows-1250") as f:
    plik_danych = csv.writer(f)

    plik_danych.writerow(["Imię i nazwisko", "m^2 pow", "Gaz", "Prąd", "Czynsz", "Woda", "Śmieci"])
    for _ in range(50):
        plik_danych.writerow([dane.name(), i(n=200), i(), i(), i(), i(), i()])
