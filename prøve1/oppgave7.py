def konverter_til_binær(tall: int) -> str:
    binærtall_streng = ""

    while tall > 0:
        binærtall_streng += str(tall % 2)
        tall //= 2

    return binærtall_streng[::-1]


def main() -> None:
    tall = int(input("Skriv et heltall som skal konverteres til binær: "))
    print(f"Tall skrevet som binær er {konverter_til_binær(tall)}")


if __name__ == "__main__":
    main()
