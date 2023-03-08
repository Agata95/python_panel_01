"""
1 klasa, która ma datę urodzenia (jako str) i wyświetla metoda info() datę urodzenia

2 klasa, która dziedzyczy z 1 i dodatkowo ma miesięczne zarobki, a info() wyswietla datę ur i zarobki
"""


class Person:
    def __init__(self, date_of_birth: str):
        self.date_of_birth = date_of_birth

    def info(self):
        print(f"Date of birth: {self.date_of_birth}")


class Employee(Person):
    def __init__(self, earnings: float, date_of_birth: str):
        super().__init__(date_of_birth)
        self.earnings = earnings

    def info(self):
        print(f"Date of birth: {self.date_of_birth}, earnings: {self.earnings}")


person = Person("18-01-1998")
person.info()

employee = Employee(30000, person.date_of_birth)
employee.info()
