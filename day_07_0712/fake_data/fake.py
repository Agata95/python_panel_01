import csv
from faker import Faker
from random import random, randint

fake_ = Faker("pl-PL")


def i(n=10000):
    return int(random() * n)


def fn_gen(rodzaj="ogolny", ilosc=30):
    with open(rodzaj + ".txt", mode='w') as f:
        writer = csv.writer(f)
        if rodzaj == "ogolny":
            writer.writerow(["Imię i nazwisko", "m^2 pow", "Gaz", "Prąd", "Czynsz", "Woda", "Śmieci"])
        elif rodzaj == "historia":
            writer.writerow(["rok", "słowiański", "germański", "celtyckie"])
        elif rodzaj == "fizyka":
            writer.writerow(["Właściciel paneli", "m^2 pow", "kw/h", "Amper", "Volt", "chłodzienie m^3/godz"])
        for _ in range(ilosc):
            if rodzaj == "ogolny":
                dane = [fake_.name(), i(n=200), i(), i(), i(), i(), i()]
            elif rodzaj == "historia":
                dane = [randint(1500, 1700), i(), i(), i()]
            elif rodzaj == "fizyka":
                dane = [fake_.name(), i(n=200), i(), i(), i(), i()]
            writer.writerow(dane)


fn_gen("ogolny", ilosc=50)
