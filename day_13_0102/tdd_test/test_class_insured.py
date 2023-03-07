import pytest
from tdd_functions.class_insured import Insured


@pytest.fixture
def one_insured():
    return Insured("XXX xxx", 2000, "boss", "Ergo Hestia")


def test_01_simple_object(one_insured):
    assert one_insured.name == "XXX xxx"


def test_02_simple_object(one_insured):
    assert one_insured.position == "boss"


def test_03_enter_capital(one_insured):
    one_insured.enter_capital(30000)
    assert one_insured.capital == 30000


def test_04_enter_capital(one_insured):
    one_insured.enter_capital(-10)
    assert one_insured.capital == 0


def test_05_earnings(one_insured):
    one_insured.enter_earnings(2022, 120000)
    assert type(one_insured.earnings) is dict


def test_06_earnings(one_insured):
    one_insured.enter_earnings(2022, 120000)
    assert one_insured.earnings == {2022: 120000}


def test_07_earnings(one_insured):
    one_insured.enter_earnings(2022, 120000)
    one_insured.enter_earnings(2021, 20000)
    assert one_insured.earnings == {2021: 20000, 2022: 120000}


def test_08_earnings(one_insured):
    one_insured.enter_earnings(2022, 120000)
    one_insured.enter_earnings(2021, 20000)
    one_insured.enter_earnings(2022, 420000)
    assert one_insured.earnings == {2021: 20000, 2022: 420000}


def test_09_earnings(one_insured):
    one_insured.enter_earnings(-5, 120000)
    one_insured.enter_earnings(2021, 20000)
    one_insured.enter_earnings(2022, "aaa")
    assert one_insured.earnings == {2021: 20000}


def test_10_earnings(one_insured):
    assert one_insured.enter_earnings(-5, 120000) is False
