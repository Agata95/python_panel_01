import pytest
from datetime import datetime


class Person:
    A_TAX = 0.06
    B_TAX = 0.12

    def __init__(self, name: str, birth: int = 1900, salary: int | float = 3300):
        """

        :param name:
        :param birth: rok urodzenia, zawsze int > 1900
        :param salary: brutto zarobki miesięczne
        """
        self.name = name
        self.birth = birth
        self.age = datetime.now().year - self.birth
        self.salary = salary
        self.group = None
        self.brutto_income = 0
        self.yearly_tax = 0
        self.netto_income = 0
        print(f"Utworzyliśmy obiekt o ID: {id(self)} / {self.name=}")

    # 3 kropki to typ danych Ellipsis
    # można nie podawać parametru group
    def yearly_income(self, group: str = ...) -> float:
        """

        :param group: grupa podatkowa
        A - zarobki do 120 000 rocznie
        B - powyżej 120 000 rocznie
        :return:
        """
        if group is Ellipsis:
            self.group = "A" if self.salary * 12 <= 120000 else "B"
        else:
            self.group = group

        self.brutto_income = (12 * self.salary)
        self.yearly_tax = self.brutto_income * self.A_TAX if self.group == "A" else self.brutto_income * self.B_TAX
        self.netto_income = float(self.brutto_income - self.yearly_tax)
        return self.netto_income


# Teraz szykujemy dane:
@pytest.fixture
def list_of_persons():
    return [Person("Adam Old"), Person("Beata", 1970), Person("Szymon", 2004, 3301)]


@pytest.fixture
def list_of_persons2():
    return [Person("Adam Old"), Person("Beata", 1970), Person("Szymon", 2004, 3301), Person("Otton", 1800, 45000)]


# a teraz wykorzystujemy fixture w testach
def test_01(list_of_persons):
    for person in list_of_persons:
        assert type(person.yearly_income()) is float


def test_02(list_of_persons):
    for person in list_of_persons:
        assert person.yearly_income() >= 100


def test_03(list_of_persons):
    for person in list_of_persons:
        assert person.yearly_income() >= 10000


def test_04(list_of_persons):
    for person in list_of_persons:
        assert person.yearly_income() >= 1000000


def test_05(list_of_persons2):
    for person in list_of_persons2:
        assert person.yearly_income() >= 1000000
