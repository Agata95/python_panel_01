from datetime import date

print("Importy date...")


class Ubezpieczony:
    def __init__(self, name: str, birthdate: str, address: str):
        self.name = name
        self.birthdate = birthdate
        self.age = date.today().year - int(birthdate[:4])
        self.address = address
        self.pesel = None
        self.__lata_bezszkodowosci = 0
        print(f"Utworzyliśmy obiekt o ID: {id(self)} / {self.name=}")

    def info(self):
        print(f"Ubezpieczony: {self.name}, urodzony w {self.birthdate}, ma lat:{self.age}")

    def old(self):
        return self.age
