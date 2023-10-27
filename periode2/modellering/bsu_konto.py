from bankkonto import Bankkonto
from person import Person


class BSUKonto(Bankkonto):
    def __init__(
        self, eier: Person, kontonummer: str, maks_årlig_beløp_innsetting: float
    ) -> None:
        super().__init__(eier, kontonummer)

        self._maks_årlig_beløp_innsetting = maks_årlig_beløp_innsetting
        self._årlig_beløp_innsetting = 0

    def motta_beløp(self, beløp: float) -> float:
        if self._årlig_beløp_innsetting == self._maks_årlig_beløp_innsetting:
            print()
            print(
                f"Du har allerede satt {self._maks_årlig_beløp_innsetting} kr inn på kontoen"
            )
            print("Du kan ikke sette inn et nytt beløp før neste år")

            return self._saldo

        if self._årlig_beløp_innsetting + beløp > self._maks_årlig_beløp_innsetting:
            print()
            print(f"Du prøvde å sette {beløp} kr inn på kontoen")
            print("Dette tar deg over grensen for årlig innsetting av penger")

            return self._saldo

        saldo_ble_endret = self._saldo != super().motta_beløp(beløp)

        if saldo_ble_endret:
            self._årlig_beløp_innsetting += beløp

        return self._saldo


def main() -> None:
    person = Person("Hege", "Hermansen", "000 00 000")
    konto = BSUKonto(person, "1983918291", 4000)

    konto.motta_beløp(3000)
    konto.motta_beløp(2000)
    konto.motta_beløp(1000)
    konto.motta_beløp(300)

    print(konto)


if __name__ == "__main__":
    main()
