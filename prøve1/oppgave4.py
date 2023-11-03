import random


def sum_tilfeldig_tall(antall: int, nedre_grense: int, øvre_grense: int) -> int:
    return sum(random.randint(nedre_grense, øvre_grense) for _ in range(antall))


def main() -> None:
    print(f"Summen av 19 tilfeldige tall er {sum_tilfeldig_tall(19, 1, 10)}")


if __name__ == "__main__":
    main()
