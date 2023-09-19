import re

WORD_REGEX = re.compile(r"([^\s]+)")


def count_words(text: str) -> int:
    return len(WORD_REGEX.findall(text))


def main() -> None:
    assert count_words("abc def") == 2
    assert count_words("") == 0
    assert count_words("hdjhfc c hjkfkh    jhkfbjhkd   hjk") == 5


if __name__ == "__main__":
    main()
