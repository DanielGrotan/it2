import math


def main() -> None:
    numbers: list[float] = []
    smallest_number = math.inf

    while True:
        try:
            number = float(input("Skriv inn et tall: "))
        except ValueError:
            continue

        numbers.append(number)

        smallest_number = min(smallest_number, number)

        if number > 10:
            break

    print(f"Det minste tallet er: {smallest_number}")
    print(f"Det største tallet er: {numbers[-1]}")

    average = sum(numbers) / len(numbers)

    print(f"Gjennomsnittet av tallene du har skrevet inn er: {average}")


if __name__ == "__main__":
    main()
