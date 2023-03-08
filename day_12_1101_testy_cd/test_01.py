# uruchamiamy pytest test_01.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def test_answer2():
    assert inc(3) == 4


# poniższy się nie wykonuje, nie nazywa się od test_
def test_answer3():
    assert inc(3) == 4
