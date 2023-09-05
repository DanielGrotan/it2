def main() -> None:
    temperature, letter = input("Skriv inn temperatur (123 F eller 123 C): ").split(" ")

    temperature = float(temperature)

    if letter == "F":
        converted_temperature = 5 / 9 * (temperature - 32)
        converted_letter = "C"
    else:
        converted_temperature = temperature * 9 / 5 + 32
        converted_letter = "F"

    print(
        f"{temperature} {letter} er det samme som {converted_temperature} {converted_letter}"
    )


if __name__ == "__main__":
    main()
