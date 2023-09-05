def main() -> None:
    while True:
        try:
            age = int(input("Skriv inn alderen din: "))
        except ValueError:
            continue

        if age < 0:
            print("Alderen din kan ikke være negativ")
            continue

        print(f"Du er {age} år gammel")
        break


if __name__ == "__main__":
    main()
