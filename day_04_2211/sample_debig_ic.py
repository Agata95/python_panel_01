from icecream import ic


def function_test(parameter):
    return parameter + 5


value = function_test(5)
print(value)

# now how to debug:
ic(function_test(5))
