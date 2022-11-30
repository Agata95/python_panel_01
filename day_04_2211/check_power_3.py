import math

"""
check if datas in file are power of 3 and count it
read numbers from file `liczby.txt` and count all of the power of 3
"""

powers = [3 ** x for x in range(1, 20)]


def counting(data_int):
    list_nums = [num for num in data_int if num in powers and num]

    return len(list(dict.fromkeys(list_nums)))


def open_file(path):
    with open(path) as file:
        number_list = file.readlines()
    return [int(num) for num in number_list]


list_of_num = open_file('liczby.txt')
result = counting(list_of_num)

print(f"In file are {result} numbers that are powers of 3.")
