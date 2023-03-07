from day_11_2812_testy.tests_production.files_to_test.ubezpieczeni import Ubezpieczony


def test_old_01():
    person = Ubezpieczony("Name_1", "1974-11-03", "Warszawa")
    assert person.old() == 49
