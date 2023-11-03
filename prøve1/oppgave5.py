def tell_siffer(tall: int) -> list[int]:
    siffer_telling = [0] * 10

    for siffer in str(tall):
        siffer_telling[int(siffer)] += 1

    return siffer_telling


def main() -> None:
    tall = 21732546725176452198378341032303020120

    print(f"Siffer tellinger {tell_siffer(tall)}")


if __name__ == "__main__":
    main()
