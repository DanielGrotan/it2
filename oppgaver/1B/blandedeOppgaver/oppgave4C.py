def main() -> None:
    largest_number = max(
        map(int, input('Skriv inn tre tall separert med ", ": ').split(", "))
    )

    print(f"Det største tallet er: {largest_number}")


if __name__ == "__main__":
    main()
