from day_02_1811.utils import calculator

# Day 02 challenge - Calculator
# - You are given two symbols and a sign
# - Check the sign and perform the right operation on the input
# - Print the result

# Examples:
# 1 + 1 -> 2
# 2 * 4 -> 8

# This is the main file, checking your solution
# Write your solution in utils.py

if __name__ == '__main__':
    assert(calculator(1, '+', 1) == 2)
    print('Test 01 - ok!')
    assert(calculator(2, '*', 4) == 8)
    print('Test 02 - ok!')
    assert(calculator(2, '/', 4) == 0.5)
    print('Test 03 - ok!')
