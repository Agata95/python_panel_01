"""
Program:
zmienna typu list i 2 funkcje

1 funkcja, która sprawdzi, czy jej parametr jest typu str i jeśli tak, doda go do listy
2 funkcja, ktora wyswietli wartość indeksu listy, który jest jej parametrem, a jeśli lista jest krótsza,
to wypisze na ekranie informację o błędzie i zwróci wartość False
"""


def first(word):
    str_list = []
    if isinstance(word, str):
        str_list.append(word)
    return str_list


def second(value_list, index):
    try:
        value = value_list[index]
        print(value)
        return value
    except Exception as ex:
        print(ex)
        return False


first("word")
first(45)
first("Alexa")
second([2, 6, 45, "A", "test", [0, 3, 4]], 5)
second([2, 6, 45, "A", "test", [0, 3, 4]], 82)
second([2, 6, 45, "A", "test", [0, 3, 4]], 3)
second([2, 6, 45, "A", "test", [0, 3, 4]], 7)

if __name__ == "__main__":
    assert (first("word") == ["word"])
    print("Test 01 done!")
    assert (first(45) == [])
    print("Test 02 done!")
    assert (first("Alexa") == ["Alexa"])
    print("Test 03 done!")
    assert (second([2, 6, 45, "A", "test", [0, 3, 4]], 5) == [0, 3, 4])
    print("Test 04 done!")
    assert (not second([2, 6, 45, "A", "test", [0, 3, 4]], 82))
    print("Test 05 done!")
    assert (second([2, 6, 45, "A", "test", [0, 3, 4]], 3) == "A")
    print("Test 06 done!")
    assert (not second([2, 6, 45, "A", "test", [0, 3, 4]], 7))
    print("Test 07 done!")
