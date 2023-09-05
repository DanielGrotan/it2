import functools


def length_1(string: str) -> int:
    return len(string)


def length_2(string: str) -> int:
    length = 0

    for _ in string:
        length += 1

    return length


def length_3(string: str) -> int:
    length = 0

    try:
        while True:
            string[length]
            length += 1
    except IndexError:
        return length


def length_4(string: str) -> int:
    ...  # ???????????????????????????


def length_5(string: str) -> int:
    return functools.reduce(lambda a, _: a + 1, string, 0)


def length_6(string: str) -> int:
    return sum(1 for _ in string)
