# Enumerators examples

def return_two_variables():
    index = 1
    element = 'one'
    return index, element


if __name__ == '__main__':
    for element in [1, 2, 3, 4]:
        print(element)

    # now lets try a variable that is a collection
    collection = [1, 2, 3, 4]
    for element in collection:
        print(element)

    # now with strings
    collection = ['one', 'two', 'three']
    for element in collection:
        print(element)

    # range
    for element in range(3):
        print(element)

    # range as index
    collection = ['one', 'two', 'three']
    for element in range(3):
        print(collection[element])

    # enumerators at last
    collection = ['one', 'two', 'three']
    for enumerator in enumerate(collection):
        print(enumerator)

    # enumerators at last
    collection = ['one', 'two', 'three']
    for index, element in enumerate(collection):
        print(f'Collection[{index}] equals: {element}')

    i, el = return_two_variables()
    print(i, el)

    enumerator = return_two_variables()
    print(enumerator)

