import random


def main() -> None:
    throws = int(input("Skriv inn antall kast: "))

    sum_ = 0

    for _ in range(throws):
        first_dice_throw = random.randint(1, 6)
        second_dice_throw = random.randint(1, 6)

        print(f"Første kast: {first_dice_throw}")
        print(f"Andre kast: {second_dice_throw}")

        sum_ += first_dice_throw + second_dice_throw

    average = sum_ / (throws * 2)

    print(f"Gjennomsnittet av kastene er: {average}")


if __name__ == "__main__":
    main()
