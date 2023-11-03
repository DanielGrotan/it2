def kvadrer_tall(start: int, slutt: int, steg: int) -> None:
    for tall in range(start, slutt, steg):
        print(tall**2)


def main() -> None:
    kvadrer_tall(9, 0, -1)


if __name__ == "__main__":
    main()
