from collections import Counter


def main() -> None:
    text = "Excepteur sit dolor nostrud ullamco qui exercitation pariatur qui officia nulla culpa ullamco occaecat."

    letter_count = Counter(text)
    print(letter_count)


if __name__ == "__main__":
    main()
