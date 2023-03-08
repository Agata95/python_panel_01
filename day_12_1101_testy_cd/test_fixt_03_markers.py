import pytest
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


# Teraz szykujemy dane:
@pytest.fixture
def list_of_persons():
    return [Person("Adam Old", 5500), Person("Beata", 1970, 150), Person("Szymon", 2004, 3301)]


@pytest.fixture
def list_of_persons_with_tax_grup(list_of_persons):
    temp = list_of_persons[:]
    temp[1].set_group("B")
    temp[2].set_group("B")
    return temp


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


@pytest.mark.dziwne
def test_05(list_of_persons_with_tax_grup):
    for person in list_of_persons_with_tax_grup:
        assert person.yearly_income() >= 10000, f"{person.name=} / {person.yearly_income()} >= 10000"

# wywołujemy:  pytest -v -m dziwne | pytest -v -m "not dziwne"
# więcej info: https://docs.pytest.org/en/7.1.x/example/markers.html#adding-a-custom-marker-from-a-plugin
