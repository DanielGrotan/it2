def reverse_1(string: str) -> str:
    result = ""

    for i in range(1, len(string) + 1):
        result += string[-i]

    return result


def reverse_2(string: str) -> str:
    if not string:
        return ""

    return reverse_2(string[1:]) + string[0]


def reverse_3(string: str) -> str:
    return string[::-1]


def reverse_4(string: str) -> str:
    return "".join(reversed(string))


def reverse_5(string: str) -> str:
    return "".join(string[-i] for i in range(1, len(string) + 1))
