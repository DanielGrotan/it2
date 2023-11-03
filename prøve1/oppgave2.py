from typing import Literal

BitStatus = Literal[0, 1]


def antall_aktive_bits(binærtall: list[BitStatus]) -> int:
    return sum(binærtall)


def main() -> None:
    binærtall: list[BitStatus] = [1, 0, 0, 0, 1, 1, 0]

    print(
        f"Antallet aktive bits i binærtallet 1000110 er {antall_aktive_bits(binærtall)}"
    )


if __name__ == "__main__":
    main()
