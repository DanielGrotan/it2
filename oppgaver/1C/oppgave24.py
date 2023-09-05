def main() -> None:
    while True:
        try:
            month_number = int(input("Oppgi nummeret til måneden vi er i: "))
        except ValueError:
            continue

        if 1 <= month_number <= 12:
            print(f"Du skrev inn {month_number}")
            break

        print("Du må oppgi et tall mellom 1 og 12")


if __name__ == "__main__":
    main()
