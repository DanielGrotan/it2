def main() -> None:
    numbers: list[int] = []
    seen: set[int] = set()

    while True:
        number = int(input("Skriv et tall: "))

        if number in seen:
            print("Dette tallet er allerede i listen")
            continue

        numbers.append(number)
        seen.add(number)

        if len(numbers) == 10:
            break

    print(f"Listen din er: {numbers}")


if __name__ == "__main__":
    main()
