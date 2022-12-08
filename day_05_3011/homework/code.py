import string

values_all_list = [113, 77, 101, 101, 77, 77, 107, 107, 107, 118, 107, 77, 107, 113, 118, 113, 77, 77, 77, 77, 113, 77, 101, 118, 113, 107, 113, 118, 107, 77, 108, 101, 107, 118, 77, 108, 118, 101, 77, 113, 77, 113, 107, 77, 108, 118, 118, 107, 113, 108, 101, 118, 113, 77, 101, 101, 107, 101, 77, 108, 118, 77, 107, 77, 108, 101, 101, 101, 77, 107, 77, 77, 107, 108, 113, 107, 107, 107, 113, 107, 108, 107, 77, 113, 108, 101, 101, 101, 113, 113, 107, 108, 118, 118, 101, 77, 118, 113, 113, 118]
values_list = list(dict.fromkeys(values_all_list))
alphabet = list(string.ascii_uppercase)

ascii_list = [chr(value).upper() for value in values_list]
result_list = []

for el in ascii_list:
    for index, value in enumerate(alphabet):
        if el == value:
            result_list.append(alphabet[index - 3])

print(alphabet)
print(ascii_list)
print(result_list)
