import random


def main() -> None:
    number = random.randint(1, 101)
    guesses = 10

    for _ in range(guesses):
        guess = int(input("Gjett tallet: "))

        if guess == number:
            print("Du gjettet riktig")
            break

        if guess > number:
            print("Tallet du gjettet er for høyt")
        else:
            print("Tallet du gjettet er for lavt")
    else:
        print("Du klarte ikke å gjette tallet")


if __name__ == "__main__":
    main()
