import random


def main() -> None:
    throws = int(input("Skriv inn antall kast: "))

    sum_ = 0

    for _ in range(throws):
        dice_throw = random.randint(1, 6)
        print(f"Kast: {dice_throw}")

        sum_ += dice_throw

    average = sum_ / throws

    print(f"Gjennomsnittet av kastene er: {average}")


if __name__ == "__main__":
    main()
