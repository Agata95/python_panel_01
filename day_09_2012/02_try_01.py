from icecream import ic
import timeit

"""
konstrukcja try: ... except ...

"""


def my_division_function_asrt(base: int | float, divider: int | float) -> int | float:
    assert divider != 0, "Nie dzielimy przez zero"
    return base / divider


def my_division_function_std(base: int | float, divider: int | float) -> int | float:
    # assert divider != 0, "Nie dzielimy przez zero"
    return base / divider


def my_division_function_try(base: int | float, divider: int | float) -> int | float:
    # assert divider != 0, "Nie dzielimy przez zero"
    try:
        return base / divider
    except:
        return False
    # except (Exception,): - znika E722


ic(timeit.timeit(lambda: my_division_function_asrt(10, 4), number=9999999))
ic(timeit.timeit(lambda: my_division_function_std(10, 4), number=9999999))
# ok, ale co będzie, gdy dzielimy przez zero?
# ic(my_division_function_std(3, 0))
ic(my_division_function_try(3, 0))

"""
ic| timeit.timeit(lambda: my_division_function_asrt(10, 4), number=9999999): 1.3635511889988265
ic| timeit.timeit(lambda: my_division_function_std(10, 4), number=9999999): 1.1240981060000195
ic| my_division_function_try(3, 0): False
"""
