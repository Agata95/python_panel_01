def divisibility(value):
    """value should be an integer number"""

    if type(value) is not int:
        return False
    if value < 11:
        return False

    output_list = []
    for number in range(2, 10):  # 540003 function calls in 3.208 seconds
    # for number in (2, 3, 4, 5, 6, 7, 8, 9, 10):  # 540003 function calls in 2.695 seconds
        if value % number == 0:
            output_list.append(number)

    if output_list:
        return f"For {value} we have: {output_list}"
    else:
        return f"Value {value} it's a prime number"


# wczytanie danych z pliku
with open('liczby.txt', 'r') as file:
    numbers_list = file.readlines()

data_int = [int(num) for num in numbers_list]
messages = [divisibility(element) for element in data_int if isinstance(divisibility(element), str)]

with open('numbers_div.txt', 'w') as file:
    for el in messages:
        file.writelines(el)
        file.writelines('\n')

