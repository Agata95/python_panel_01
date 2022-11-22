def divisibility(value):
    """value should be an integer number"""

    if type(value) is not int:
        return False
    if value < 11:
        return False

    output_list = []
    # for number in range(2, 10):  # 540003 function calls in 3.208 seconds
    for number in (2, 3, 4, 5, 6, 7, 8, 9, 10):  # 540003 function calls in 2.695 seconds
        if value % number == 0:
            output_list.append(number)

    if output_list:
        return f"For {value} we have: {output_list}"
    else:
        return f"Value {value} it's a prime number"


# przykładowe wywołanie
for _ in range(100000):
    for some_value in [
        False,
        1,
        "Adam",
        10,
        11,
        22,
        234,
        456,
        654,
        2345,
        4444,
        4536,
        432523452,
    ]:
        print(divisibility(some_value))
