from datetime import datetime


class Person:
    A_TAX = 0.06
    B_TAX = 0.12

    def __init__(self, name: str, birth: int = 1900, salary: int | float = 3300, group: str = ...):
        """

        :param name:
        :param birth: rok urodzenia, zawsze int > 1900
        :param salary: brutto zarobki miesięczne
        :param group: Grupa podatkowa A|B lub domyślnie ... i liczymy
        """
        self.name = name
        self.birth = birth
        self.age = datetime.now().year - self.birth
        self.salary = salary
        self.brutto_income = 0
        self.yearly_tax = 0
        self.netto_income = 0

        if group is Ellipsis:
            self.group = "A" if self.salary * 12 <= 120000 else "B"
        else:
            self.group = group

        print(f"Utworzyliśmy obiekt o ID: {id(self)} / {self.name=}")

    def set_group(self, group: str) -> bool:
        """

        :param group: A|B
        :return: True if group has changed, otherwise False
        """
        if self.group == group:
            ret = True
        else:
            ret = False
        self.group = group
        return ret

    def yearly_income(self) -> float:

        self.brutto_income = (12 * self.salary)
        self.yearly_tax = self.brutto_income * self.A_TAX if self.group == "A" else self.brutto_income * self.B_TAX
        self.netto_income = float(self.brutto_income - self.yearly_tax)
        return self.netto_income
