"""
Funkcja, która mnoży dwie liczby, a jesli wynik jest ujemny, to wywołuje
błąd raise Exception('Wynik jest ujemny...')
"""


def multiply_numbers(number_1: int | float, number_2: int | float) -> int | float:
    result = number_1 * number_2
    if result >= 0:
        return result
    else:
        raise Exception('Result is negative!')


print(multiply_numbers(4, 5))
print(multiply_numbers(4.0, 0))
print(multiply_numbers(5, 6.2))
print(multiply_numbers(4, -10))
