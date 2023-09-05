import random


def main() -> None:
    numbers = list(random.randint(-100, 100) for _ in range(50))

    print(f"Tall: {numbers}")

    # a
    even_numbers = list(filter(lambda number: number % 2 == 0, numbers))
    print(f"Partall: {even_numbers}")

    # b
    odd_numbers = list(filter(lambda number: number % 2 == 1, numbers))
    print(f"Oddetall: {odd_numbers}")

    # c
    even_number_indices = numbers[::2]
    print(f"Tall med partallsindeks: {even_number_indices}")

    # d
    reversed_numbers = numbers[::-1]
    print(f"Omvendt rekkefølge: {reversed_numbers}")


if __name__ == "__main__":
    main()
