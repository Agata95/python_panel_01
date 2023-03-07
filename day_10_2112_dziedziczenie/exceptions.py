class MyException(Exception):
    """Raised when something will go wrong with our application"""
    pass


# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise MyException
    else:
        print("Eligible to Vote")

except MyException:
    print("Exception occurred: Invalid Age")


