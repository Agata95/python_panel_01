class Pojazd:
    """Pojazd ogólny - i ilość pojazdów"""
    flota = 0

    def __init__(self, rodzaj: str, kolor: str):
        self.rodzaj = rodzaj
        self.kolor = kolor
        self.__doors = None
        Pojazd.flota += 1
        self.id = id(self)
        print(f"Utworzono {self.id=}")

    # wywoływana gdy wywołujemy metodę del
    # lub gdy skończy się skrypt
    # DESTRUKTOR
    def __del__(self):
        """wszystko co tu jest, wykonuje się
        podczas del() i na końcu skryptu"""
        print(f"Skasowano z pamięci {self.id=}")
        Pojazd.flota -= 1
        print(self.how_many())

    def info(self) -> str:
        return f"Pojazd rodzaju {self.rodzaj} i kolorze {self.kolor}"

    def how_many(self):
        return f"Wszystkich Pojazdów {Pojazd.flota}"

    # dekorator classmethod mówi, że będziemy się odwoływać do klasy, a nie obiektu
    # przyjmuje parametr cls, czyli nazwę klasy
    # zwracać będzie ilość pojazdów dla konkretnej klasy
    @classmethod
    def how_many_2(cls):
        return f"Wszystkich Pojazdów {cls.flota}"

    @property
    def doors(self):
        return self.__doors

    # dekorator pozwala ustawiać liczbę drzwi
    # sprawdzając, czy drzwi są w zakresie od 2 do 5
    @doors.setter
    def doors(self, doors):
        if 2 < doors < 5:
            self.__doors = doors


class Mercedes(Pojazd):

    def __init__(self, kolor: str, rok_produkcji: int, przebieg: int):
        # uruchamiamy metodę init z klasy Pojazd
        # dzięki temu nadpiszemy, że rodzaj samochodu to zawsze 'Mercedes"
        super().__init__("Mercedes", kolor)
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg


class VW(Pojazd):

    def __init__(self, kolor: str, rok_produkcji: int, przebieg: int):
        super().__init__("VW", kolor)
        self.rok_produkcji = rok_produkcji
        self.przebieg = przebieg


pojazd1 = Pojazd("merc", "zielony")
pojazd2 = Pojazd("VW", "czarny")
pojazd3 = Mercedes("niebieski", 2005, 123000)
pojazd4 = VW("srebrny", 2015, 27000)

pojazd1.doors = 4

print(pojazd1.how_many())
print(pojazd1.how_many_2())

del (pojazd1)

# print(pojazd1.how_many())
print(Pojazd.how_many_2())
print("-------KONIEC--------")

# print(Pojazd.how_many_2())
# print(pojazd1.how_many())
