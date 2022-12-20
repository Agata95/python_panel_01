def my_division_function_try(base: int | float, divider: int | float) -> int | float:
    # assert divider != 0, "Nie dzielimy przez zero"
    try:
        return base / divider
    except Exception as e:
        return f"Some error - {e}"


print(my_division_function_try(3, 0))


def my_division_function_try_exc(base: int | float, divider: int | float) -> int | float:
    # assert divider != 0, "Nie dzielimy przez zero"
    try:
        return base / divider
    except ZeroDivisionError:
        return "Nie dzielimy przez zero!"
    except TypeError:
        return "ERROR - typ"


print(my_division_function_try_exc("3", 0))


def my_division_function_try_exc_f(base: int | float, divider: int | float) -> int | float:
    # assert divider != 0, "Nie dzielimy przez zero"
    try:
        return base / divider
    except ZeroDivisionError:
        return "Nie dzielimy przez zero!"
    except Exception as e:
        raise Exception(f'Some error - {e}')
    finally:
        print("A tak czy inaczej...")


print(my_division_function_try_exc_f(3, 0))
print(my_division_function_try_exc_f(3, "A"))
