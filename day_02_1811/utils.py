import string


def reverse_words(sentence):
    sentence_list = sentence.split()
    element_list = [element[::-1] if len(element) > 4 else element for element in sentence_list]

    return ' '.join(element_list)


def caesar_shift(sentence):
    alphabet = list(string.ascii_uppercase)
    sentence_list = sentence.split()
    element_list = []

    for s in sentence_list:
        word = ''
        for el in s:
            for a in alphabet:
                if el == a:
                    index = alphabet.index(a)
                    try:
                        word += alphabet[index - 3]
                    except:
                        index = (len(alphabet) - index - 4)
                        word += alphabet[index - 1]

        element_list.append(word)

    return ' '.join(element_list)


def caesar_shift_decoder(sentence):
    alphabet = list(string.ascii_uppercase)
    sentence_list = sentence.split()
    element_list = []

    for s in sentence_list:
        word = ''
        for el in s:
            for a in alphabet:
                if el == a:
                    index = alphabet.index(a)
                    try:
                        word += alphabet[index + 3]
                    except:
                        index = -(len(alphabet) - index - 4)
                        word += alphabet[index - 1]

        element_list.append(word)

    return ' '.join(element_list)


def calculator(number_1, sigh, number_2):
    result = 0
    if sigh == '+':
        result = number_1 + number_2
    elif sigh == '-':
        result = number_1 - number_2
    elif sigh == '*':
        result = number_1 * number_2
    elif sigh == '/':
        result = number_1 / number_2

    return result
