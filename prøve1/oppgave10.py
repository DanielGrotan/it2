def fizz_buzz(antall: int) -> None:
    for tall in range(1, antall + 1):
        if tall % 15 == 0:
            print("Fizz-Buzz")
        elif tall % 3 == 0:
            print("Fizz")
        elif tall % 5 == 0:
            print("Buzz")
        else:
            print(tall)


def main() -> None:
    fizz_buzz(15)


if __name__ == "__main__":
    main()
