"""
ubezpieczony ma dane ... itp ...
mamy ubezpieczonych ...
co możemy z ubezpieczonym zrobić ...
"""
from datetime import date


class Insured:
    # konstruktor
    def __init__(self, name: str, date_of_birth: str, address: str):
        self.name = name
        self.date_of_birth = date_of_birth
        self.age = int(str(date.today())[:4]) - int(date_of_birth[:4])
        self.address = address
        self.pesel = None
        # jeśli damy __ to jej 'oficjalnie' nie ma, nie wywołamy jej poza def
        self.__years_no_claims = 0

        print(f"Utworzyliśmy obiekt o ID: {id(self)}")

    def info(self):
        print(f"Insured: {self.name}, date of birth is {self.date_of_birth}, are {self.age} years old, address is {self.address}.")


insured_1 = Insured("Pszczółka Maja", "1990-10-10", "Ogród")
insured_2 = Insured("Gucio", "1982-12-10", "Ogród")

print(id(insured_1))
print(id(insured_2))

print(insured_1.name, insured_1.date_of_birth, insured_1.age)
print(insured_2.name, insured_2.date_of_birth, insured_2.age)

insured_1.info()
insured_2.info()

insured_1.__years_no_claims = -20
print(insured_1.__years_no_claims)
