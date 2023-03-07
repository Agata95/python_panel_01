class Pojazd:
    def __init__(self, nazwa: str, rok: int):
        self.nazwa = nazwa
        self.rok = rok

    def info(self) -> str:
        return f"To pojazd ogólny - {self.nazwa} / {__class__.__name__}"

    def rok_prod(self) -> str:
        return f"Rok produkcji to {self.rok}"


pojazd_1 = Pojazd("mysza", 2003)
print(pojazd_1.info())
print(pojazd_1.rok_prod())


class Van(Pojazd):
    def __init__(self, nazwa, rok):
        self.nazwa = nazwa
        self.rok = rok


van = Van("sharan-baranek", 2014)

print(pojazd_1.info())
print(pojazd_1.rok_prod())

print(van.info())
# print(van.rok_prod())
