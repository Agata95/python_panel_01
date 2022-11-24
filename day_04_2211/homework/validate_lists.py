def is_sequence_valid(input_list: list, test_list: list) -> bool:
    """
    :param input_list: main list, for example [5, 1, 22, 6, 21, 7, 5, 7, 8]
    :param test_list: test, for example [1, 6, 21, 7]
    :return: True in this example
    """
    result_list = [test_num for test_num in test_list for input_num in input_list if test_num == input_num]

    # remove duplicates from list
    result_list = list(dict.fromkeys(result_list))

    return test_list == result_list


if __name__ == "__main__":
    assert is_sequence_valid([5, 1, 22, 21, 7, 5, 7, 8], [1, 6, 21, 7]) is False
    print("test 1 ok")
    assert is_sequence_valid([5, 1, 22, 6, 21, 7, 5, 7, 8], [1, 6, 21, 7]) is True
    print("test 2 ok")
