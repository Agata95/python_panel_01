# basic function that prints sth - just run it
def funk():
    print("Hello from funk!")


# Here you will get a string return - you can then print it in main
def get_introduction():
    return "Hello!"


# Here you will get a string return - you can then print it in main
def get_introduction():
    return "Hello!"


# Here you can pass the parameter, but you don't have to. Default is x=10. Try both ways
def get_10x_value(x=10):
    return x * 10


# This returns two values - catch them and print
def get_values():
    return 42, 0


if __name__ == '__main__':
    funk()
