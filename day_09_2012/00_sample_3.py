from datetime import datetime
import timeit
from icecream import ic
from functools import lru_cache

"""
pokazuję lru_cache
"""

def my_function(age: int) -> str:
    ret_str = f"You are {age} years old. "
    if age >= 18:
        ret_str += "And you are adult."
    else:
        ret_str += f" And you still need {18 - age} years to be an adult"

    return ret_str


def my_function_precondition(age: int) -> str:
    """
    assert expression[, assertion_message]
    if expression is false, then the statement throws an AssertionError.
    """
    assert isinstance(age, int)

    assert isinstance(age, int), f"Typ wejściowy: {type(age)}"
    assert age > 1, f"Zbyt mały wiek -> {age}"

    ret_str = f"You are {age} years old. "
    if age >= 18:
        ret_str += "And you are adult."
    else:
        ret_str += f" And you still need {18 - age} years to be an adult"

    return ret_str


"""
n general, the LRU cache should only be used when you want to reuse previously computed values.
https://docs.python.org/3/library/functools.html
"""
@lru_cache()
def my_function_postcondition(age: int) -> int:
    assert isinstance(age, int), f"Typ wejściowy: {type(age)}"
    assert age > 1, f"Zbyt mały wiek -> {age}"

    birth = datetime.today().year - age

    assert isinstance(birth, int), f"Typ zwracanej danej: {type(birth)}"
    return birth


# test prędkości - domyślnie 1 000 000 razy
# https://docs.python.org/3/library/timeit.html
print(timeit.timeit(lambda: my_function_postcondition(30), number=9999999))

# icecream
ic(timeit.timeit(lambda: my_function_postcondition(30), number=9999999))