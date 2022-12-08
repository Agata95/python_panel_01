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

caesar_shift([113, 77, 101, 107, 118, 108], 'encoder')

def calculator(a: float, sign: str, b: float):
    return eval(str(a) + str(sign) + str(b))


def check_sudoku(sudoku):
    for element in sudoku:
        for number in range(1, 10):
            if number not in element:
                return False

    return True
