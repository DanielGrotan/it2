import math


def get_middle_letters(text: str) -> str:
    return text[math.ceil(len(text) / 2) - 1 : len(text) // 2 + 1]


def main() -> None:
    assert get_middle_letters("123") == "2"
    assert get_middle_letters("1234") == "23"
    assert get_middle_letters("123456789") == "5"
    assert get_middle_letters("1234567890") == "56"


if __name__ == "__main__":
    main()
