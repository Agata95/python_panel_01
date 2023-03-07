import pytest
from tdd_functions.class_insured import Insured
from tdd_functions.edit_data import *


@pytest.fixture
def one_insured():
    i = Insured("XXX xxx", 2000, "boss", "Ergo Hestia")
    i.earnings(2022, 50000)
    i.earnings(2021, 40000)
    return i


def test_01_new_insured():
    i_tmp = add_insured()
    assert isinstance(i_tmp, Insured)