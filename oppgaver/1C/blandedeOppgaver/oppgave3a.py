def main() -> None:
    # antar at 0 ikke er et postivt heltall

    end = int(input("Skriv inn det siste positive heltallet: "))

    numbers = list(range(1, end + 1))

    average = sum(numbers) / len(numbers)

    print(f"Gjennomsnittet er: {average}")


if __name__ == "__main__":
    main()
