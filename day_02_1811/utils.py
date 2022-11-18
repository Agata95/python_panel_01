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
                    word += alphabet[index-3]
        element_list.append(word)

    return ' '.join(element_list)
