import pytest

from files_to_test.ubezpieczeni import Ubezpieczony


@pytest.fixture
def list_of_persons():
    return [Ubezpieczony("Name_1", "1974-11-03", "Warszawa"), Ubezpieczony("adam", "1970-11-03", "Warszawa"), Ubezpieczony("Bad", "11-03-1974", "Warszawa")]


def test_old_01(list_of_persons):
    for person in list_of_persons:
        assert person.old() == 49


def test_old_02(list_of_persons):
    for person in list_of_persons:
        assert person.old() > 11


def test_old_03(list_of_persons):
    for person in list_of_persons:
        assert person.old() == 48
