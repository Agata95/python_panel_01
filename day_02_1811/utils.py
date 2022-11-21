import string


def reverse_words(sentence):
    sentence_list = sentence.split()
    element_list = [element[::-1] if len(element) > 4 else element for element in sentence_list]

    return ' '.join(element_list)


def caesar_shift(sentence, action):
    alphabet = list(string.ascii_uppercase)
    word = ''

    for el in sentence:
        if el == ' ':
            word += ' '
        else:
            for index, a in enumerate(alphabet):
                if el == a:
                    if action == 'encoder':
                        try:
                            word += alphabet[index - 3]
                        except:
                            index = (len(alphabet) - index - 4)
                            word += alphabet[index - 1]
                    elif action == 'decoder':
                        try:
                            word += alphabet[index + 3]
                        except:
                            index = -(len(alphabet) - index - 4)
                            word += alphabet[index - 1]

    return word


def calculator(a: float, sign: str, b: float):
    result = 0
    if sign == '+':
        result = a + b
    elif sign == '-':
        result = a - b
    elif sign == '*':
        result = a * b
    elif sign == '/':
        result = a / b

    return result


def check_sudoku(sudoku):
    result = True
    for index, e in enumerate(sudoku):
        if result:
            for el in range(1, 10):
                if el not in e:
                    result = False
                    break
                else:
                    result = True

    return result
