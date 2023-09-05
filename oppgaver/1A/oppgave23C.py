def main() -> None:
    minutes = int(input("Skriv antall minutter: "))

    hours, minutes = divmod(minutes, 60)

    print(f"{hours} time(r) og {minutes} minutt(er)")


if __name__ == "__main__":
    main()
