def main() -> None:
    while True:
        try:
            average = float(input("Skriv inn karaktersnittet ditt: "))
        except ValueError:
            continue

        if average < 1 or average > 6:
            print("Ugyildig snitt")
            continue

        print(f"Snittet ditt er {average}")
        break


if __name__ == "__main__":
    main()
