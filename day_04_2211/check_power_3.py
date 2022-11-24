import math

"""
check if datas in file are power of 3 and count it
read numbers from file `liczby.txt` and count all of the power of 3
"""


def is_power_of_3(number):
    return (math.log(number) / math.log(3)) % 1 == 0


def counting(data_int):
    return sum([1 for num in data_int if is_power_of_3(num)])


def open_file(path):
    with open(path) as file:
        number_list = file.readlines()
    return [int(num) for num in number_list]


list_of_num = open_file('liczby.txt')
result = counting(list_of_num)

print(f"In file are {result} numbers that are powers of 3.")
