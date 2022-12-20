
"""
ubezpieczony ma dane ... itp ...
mamy ubezpieczonych ...
co możemy z ubezpieczonym zrobić ...
"""
from datetime import date
from icecream import ic
from faker import Faker
import timeit

class Ubezpieczony:
    def __init__(self, name: str, birthdate: str, address: str):
        self.name = name
        self.faker_obj = Faker("pl_PL")
        self.birthdate = birthdate
        self.age = date.today().year - int(birthdate[:4])
        self.address = address
        self.__pesel = None
        self.__lata_bezszkodowosci = 0
        print(f"Utworzyliśmy obiekt o ID: {id(self)}")

    @property
    def lata_bezszkodowosci(self):
        return self.__lata_bezszkodowosci

    @lata_bezszkodowosci.setter
    def lata_bezszkodowosci(self, ile_lat: int):
        self.__lata_bezszkodowosci = ile_lat

    def dodaj_lata_bezszkodowosci(self, ile_lat: int):
        self.__lata_bezszkodowosci += ile_lat

    def zwroc_wartosc_pesel(self):
        """
        jeśli pesel is None to wyświetl info o konieczności uruchom.
        metody wprow. pesel
        jeśli pesel jest to zwróc
        """
        return self.__pesel

    def wprowadz_pesel_1(self, pesel: str):
        """zwaliduj pesel i wprowadź gdy poprawny, a gdy nie:
        raise Exception("BAD PESEL")
        """
        cyfry_peselu = list(pesel)[:10]
        suma = 0
        wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
        l = len(cyfry_peselu)
        for el in range(len(cyfry_peselu)):
            cyfra_new = int(cyfry_peselu[el]) * int(wagi[el])
            suma += int(cyfra_new)
        reszta = suma % 10
        if reszta == 0:
            cyfra_kontr = 0
        else:
            cyfra_kontr = 10 - reszta
        if int(list(pesel)[-1]) == int(cyfra_kontr):
            self.__pesel = pesel
        else:
            # raise Exception("Błędny PESEL")
            self.__pesel = pesel

    def wprowadz_pesel_2(self, pesel: str):
        if self.faker_obj.pesel_compute_check_digit(pesel) == int(pesel[-1:]):
            self.__pesel = pesel
        else:
            # raise Exception("Błędny PESEL")
            self.__pesel = pesel

    def wprowadz_pesel_3(self, pesel: str):
        """zwaliduj pesel i wprowadź gdy poprawny, a gdy nie:
        raise Exception("BAD PESEL")
        To będziemy refaktoryzować na lekcji....
        i sprawdzać czas wykonania:
        """
        cyfry_peselu = list(pesel)[:10]
        suma = 0
        wagi = (1, 3, 7, 9, 1, 3, 7, 9, 1, 3)
        l = len(cyfry_peselu)
        for el in range(len(cyfry_peselu)):
            cyfra_new = int(cyfry_peselu[el]) * int(wagi[el])
            suma += int(cyfra_new)
        reszta = suma % 10
        if reszta == 0:
            cyfra_kontr = 0
        else:
            cyfra_kontr = 10 - reszta
        if int(list(pesel)[-1]) == int(cyfra_kontr):
            self.__pesel = pesel
        else:
            # raise Exception("Błędny PESEL")
            self.__pesel = pesel

    def info(self):
        print(f"Ubezpieczony: {self.name}, urodzony w {self.birthdate}, ma lat:{self.age}")
        print(f"PESEL: {self.__pesel}")


ubezpieczony_1 = Ubezpieczony("Adam Jurkiewicz", "1974-03-11", "Warszawa")
ic(timeit.timeit(lambda: ubezpieczony_1.wprowadz_pesel_1("74031105873"), number=9999999))
ic(timeit.timeit(lambda: ubezpieczony_1.wprowadz_pesel_2("74031105873"), number=9999999))
# nasza refaktoryzowana funkcja.
ic(timeit.timeit(lambda: ubezpieczony_1.wprowadz_pesel_3("74031105873"), number=9999999))
"""
ic| timeit.timeit(lambda: ubezpieczony_1.wprowadz_pesel_1("74031105873"), number=9999999): 33.28227858699938
ic| timeit.timeit(lambda: ubezpieczony_1.wprowadz_pesel_2("74031105873"), number=9999999): 36.438778593999814
ic| timeit.timeit(lambda: ubezpieczony_1.wprowadz_pesel_3("74031105873"), number=9999999): 31.736562134999986
"""