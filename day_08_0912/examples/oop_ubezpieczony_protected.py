"""
ubezpieczony ma dane ... itp ...
mamy ubezpieczonych ...
co możemy z ubezpieczonym zrobić ...
"""
from datetime import date


class Ubezpieczony:
    def __init__(self, name: str, birthdate: str, address: str):
        self.name = name
        self.birthdate = birthdate
        self.age = date.today().year - int(birthdate[:4])
        self.address = address
        self.__pesel = None
        self.__lata_bezszkodowosci = 0
        print(f"Utworzyliśmy obiekt o ID: {id(self)}")

    def wprowadz_pesel(self, wartosc: str):
        name = self.name.split()[0].lower()
        sex = name[-1]
        if sex == 'a' and int(wartosc[-2]) % 2 == 0:
            self.__pesel = wartosc
        elif sex != 'a' and int(wartosc[-2]) % 2 == 1:
            self.__pesel = wartosc
        else:
            raise Exception("BAD PESEL")

    def zwroc_wartosc_pesel(self):
        if not self.__pesel:
            print(f"Uruchom metodę wprowadzania peselu.")
        else:
            print(self.__pesel)
        return self.__pesel

    @property
    def lata_bezszkodowosci(self):
        return self.__lata_bezszkodowosci

    @lata_bezszkodowosci.setter
    def lata_bezszkodowosci(self, ile_lat: int):
        self.__lata_bezszkodowosci = ile_lat

    def dodaj_lata_bezszkodowosci(self, ile_lat: int):
        self.__lata_bezszkodowosci += ile_lat

    def info(self):
        print(f"Ubezpieczony: {self.name}, urodzony w {self.birthdate}, ma lat:{self.age}")
        print(f"PESEL: {self.__pesel}")


ubezpieczony_1 = Ubezpieczony("Adam Jurkiewicz", "1974-03-11", "Warszawa")
ubezpieczony_2 = Ubezpieczony("Beata Jurkiewicz", "1970-05-25", "Warszawa")

print(id(ubezpieczony_1))
print(id(ubezpieczony_2))
print(ubezpieczony_1.name)
print(ubezpieczony_2.name)
ubezpieczony_1.info()
ubezpieczony_2.info()

print("----")
print("Lata bezszodowości:")
print(ubezpieczony_2.lata_bezszkodowosci)
# print(ubezpieczony_2.__lata_bezszkodowosci)
ubezpieczony_2.lata_bezszkodowosci = 20
print(ubezpieczony_2.lata_bezszkodowosci)
ubezpieczony_2.dodaj_lata_bezszkodowosci(3)
print(ubezpieczony_2.lata_bezszkodowosci)

print("----")
print("Pesel:")
# print(ubezpieczony_1.zwroc_wartosc_pesel())
ubezpieczony_1.zwroc_wartosc_pesel()
# ubezpieczony_1.wprowadz_pesel("87236347824")
ubezpieczony_2.wprowadz_pesel("87236347824")
ubezpieczony_2.zwroc_wartosc_pesel()
# print(ubezpieczony_1.zwroc_wartosc_pesel())
# ubezpieczony_1.info()
# ubezpieczony_2.info()
