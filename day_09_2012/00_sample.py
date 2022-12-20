from datetime import datetime
import timeit


"""
For example, programmers often place assertions at the beginning of functions to check if the input is valid (preconditions).
Programmers also place assertions before functions’ return values to check if the output is valid (postconditions).
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

def my_function_postcondition(age: int) -> int:
    assert isinstance(age, int), f"Typ wejściowy: {type(age)}"
    assert age > 1, f"Zbyt mały wiek -> {age}"

    birth = datetime.today().year - age

    assert isinstance(birth, int), f"Typ zwracanej danej: {type(birth)}"
    return birth

print(my_function(48))
# print(my_function("48"))
print(my_function_precondition(48))
# print(my_function_precondition("48"))
# print(my_function_precondition(48.2))
# print(my_function_precondition(-48))
print(my_function_postcondition(20))

# test prędkości - domyślnie 1 000 000 razy
print(timeit.timeit(lambda: my_function_postcondition(30)))