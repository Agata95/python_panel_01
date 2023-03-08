from files_to_test.ubezpieczeni import Ubezpieczony


def test_old_01():
    person = Ubezpieczony("Name_1", "1974-11-03", "Warszawa")
    assert person.old() == 49


def test_old_02():
    person = Ubezpieczony("adam", "1970-11-03", "Warszawa")
    assert person.old() == 11


def test_old_03():
    person = Ubezpieczony("Bad", "11-03-1974", "Warszawa")
    assert person.old() == 48
