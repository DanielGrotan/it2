from bankkonto import Bankkonto
from person import Person


class Sparekonto(Bankkonto):
    def __init__(
        self, eier: Person, kontonummer: str, maks_årlig_antall_uttak: int
    ) -> None:
        super().__init__(eier, kontonummer)

        self._maks_årlig_antall_uttak = maks_årlig_antall_uttak
        self._årlig_antall_uttak = 0

    def ta_ut_beløp(self, beløp: float) -> float:
        if self._årlig_antall_uttak == self._maks_årlig_antall_uttak:
            print()
            print(
                f"Du har allerede tatt ut et beløp {self._maks_årlig_antall_uttak} ganger"
            )
            print("Du må vente til neste år før du kan ta ut et nytt beløp igjen")

            return 0

        penger_ble_tatt_ut = super().ta_ut_beløp(beløp) != 0

        if penger_ble_tatt_ut:
            self._årlig_antall_uttak += 1

            return beløp

        return 0


def main() -> None:
    person = Person("Hege", "Hermansen", "000 00 000")
    konto = Sparekonto(person, "173873283", 3)

    konto.motta_beløp(2000)
    konto.ta_ut_beløp(100)
    konto.ta_ut_beløp(100)
    konto.ta_ut_beløp(100)
    konto.ta_ut_beløp(200)

    print(konto)


if __name__ == "__main__":
    main()
