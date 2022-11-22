def is_sequence_valid(input_list: list, test_list: list) -> bool:
    """
    :param input_list: main list, for example [5, 1, 22, 6, 21, 7, 5, 7, 8]
    :param test_list: test, for example [1, 6, 21, 7]
    :return: True in this example
    """
    return False


if __name__ == "__main__":
    assert is_sequence_valid([5, 1, 22, 21, 7, 5, 7, 8], [1, 6, 21, 7]) is False
    print("test 1 ok")
    assert is_sequence_valid([5, 1, 22, 6, 21, 7, 5, 7, 8], [1, 6, 21, 7]) is True
    print("test 2 ok")
