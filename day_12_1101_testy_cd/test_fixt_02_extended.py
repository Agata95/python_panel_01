import pytest
from files_to_test.person_class import Person


# Teraz szykujemy dane:
@pytest.fixture
def list_of_persons():
    return [Person("Adam Old", 5500), Person("Beata", 1970, 150), Person("Szymon", 2004, 3301)]


# dwukrotnie wykorzystywanie fixture
@pytest.fixture
def list_of_persons_with_tax_group(list_of_persons):
    # kopia zawartości listy: [:]
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


@pytest.mark.max_salary
def test_05(list_of_persons_with_tax_group):
    for person in list_of_persons_with_tax_group:
        assert person.yearly_income() >= 10000, f"{person.name=} / {person.yearly_income()} >= 10000"


# trzeba dodać zamarkowany test do pytest.ini
@pytest.mark.too_old
def test_06_too_old():
    object_in_memory = True
    try:
        person = Person("Test", 1850)
        object_in_memory = True
    except Exception as e:
        object_in_memory = False

    try:
        dir(person)
        object_in_memory = True
    except NameError:
        object_in_memory = False

    assert object_in_memory == False
