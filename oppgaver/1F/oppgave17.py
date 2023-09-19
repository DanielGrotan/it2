def double_numbers(numbers: list[int]) -> list[int]:
    return list(number * 2 for number in numbers)


def main() -> None:
    numbers = [1, 2, 3, 6]
    doubled_numbers = double_numbers(numbers)

    print(f"{numbers=}, {doubled_numbers=}")


if __name__ == "__main__":
    main()
