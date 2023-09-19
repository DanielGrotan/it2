def count_letters(text: str) -> int:
    return sum(1 for _ in text)


def main() -> None:
    assert count_letters("123") == 3
    assert count_letters("") == 0


if __name__ == "__main__":
    main()
