def count_occurrences(char: str, text: str) -> int:
    count = 0

    for letter in text:
        if letter == char:
            count += 1

    return count


def main() -> None:
    assert count_occurrences("a", "ababaa") == 4
    assert count_occurrences("x", "abcd") == 0
    assert count_occurrences("d", "abnsdh") == 1


if __name__ == "__main__":
    main()
