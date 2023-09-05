import random


def main() -> None:
    # 25 tall

    numbers = list(random.randint(-100, 100) for _ in range(25))
    numbers.sort()

    print(f"Sortert liste: {numbers}")

    median = numbers[12]

    print(f"Median: {median}")

    # 50 tall
    numbers = list(random.randint(-100, 100) for _ in range(50))
    numbers.sort()

    print(f"Sortert liste: {numbers}")

    median = (numbers[24] + numbers[25]) / 2

    print(f"Median: {median}")


if __name__ == "__main__":
    main()
