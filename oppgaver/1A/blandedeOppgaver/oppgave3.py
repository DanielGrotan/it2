def main() -> None:
    months = "JanFebMarAprMaiJunJulAugSepOktNovDes"

    month_start_index = (int(input("Månedsnummer [1-12]: ")) - 1) * 3

    print(months[month_start_index : month_start_index + 3])


if __name__ == "__main__":
    main()
