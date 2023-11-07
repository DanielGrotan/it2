from bankkonto import Bankkonto
from person import Person


class BSUKonto(Bankkonto):
    def __init__(
        self, eier: Person, kontonummer: str, maks_årlig_beløp_innsetting: float
    ) -> None:
        super().__init__(eier, kontonummer)

        self.__maks_årlig_beløp_innsetting = maks_årlig_beløp_innsetting
        self.__årlig_beløp_innsetting = 0

    def motta_beløp(self, beløp: float) -> float:
        if self.__årlig_beløp_innsetting == self.__maks_årlig_beløp_innsetting:
            print()
            print(
                f"Du har allerede satt {self.__maks_årlig_beløp_innsetting} kr inn på kontoen"
            )
            print("Du kan ikke sette inn et nytt beløp før neste år")

            return self.saldo

        if self.__årlig_beløp_innsetting + beløp > self.__maks_årlig_beløp_innsetting:
            print()
            print(f"Du prøvde å sette {beløp} kr inn på kontoen")
            print("Dette tar deg over grensen for årlig innsetting av penger")

            return self.saldo

        saldo_ble_endret = self.saldo != super().motta_beløp(beløp)

        if saldo_ble_endret:
            self.__årlig_beløp_innsetting += beløp

        return self.saldo
