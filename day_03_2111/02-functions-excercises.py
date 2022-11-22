# print_variable - Write a function that:
# - takes in parameters "variable" (e.g. 0.1) and "name" (e.g. 'x')
# - prints the message "x = 0.1" with precision at two digits
def print_variable(variable: float, name: str):
    print(name, '=', variable)


# all_unique - Write a function that:
# - takes list of variables and words
# - return True if all is unique
# - return False if list have duplicates
# [1, 3, "a"] -> True
# [1, 3, "a", 1] -> False
#
# Check for lists:
# lista_a = [23, 45, 67, 67, "qw", "er", "ty", "qw"]
# lista_b = [23, 23, 45, 67, "qw", "er", "ty"]
# lista_c = [23, 45, 67, "qw", "er", "ty"]
def all_unique(var_list):
    return_list = []

    for var in var_list:
        if var not in return_list:
            return_list.append(var)

    return var_list == return_list


if __name__ == '__main__':
    print_variable(0.4, 'a')

    assert (all_unique([1, 3, "a"]) == True)
    print('Test 01 - ok!')
    assert (all_unique([1, 3, "a", 1]) == False)
    print('Test 02 - ok!')
    assert (all_unique([23, 45, 67, 67, "qw", "er", "ty", "qw"]) == False)
    print('Test 03 - ok!')
    assert (all_unique([23, 23, 45, 67, "qw", "er", "ty"]) == False)
    print('Test 04 - ok!')
    assert (all_unique([23, 45, 67, "qw", "er", "ty"]) == True)
    print('Test 05 - ok!')
