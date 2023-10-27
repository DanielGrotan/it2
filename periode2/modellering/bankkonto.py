from person import Person


class Bankkonto:
    def __init__(self, eier: Person, kontonummer: str) -> None:
        self._eier = eier
        self._kontonummer = kontonummer
        self._saldo = 0
        
        print("Nyopprettet konto:")
        print(f"  {"Eier".ljust(11)}: {self._eier}")
        print(f"  {"Kontonummer".ljust(11)}: {self._kontonummer}")
        print(f"  {"Saldo".ljust(11)}: {self._saldo}")
    
    def motta_beløp(self, beløp: float) -> float:
        if beløp <= 0:
            print()
            print(f"Du prøvde å sette inn {beløp} kr")
            print("Du kan kun sette inn et beløp som er større enn 0 kr")

            return self._saldo

        self._saldo += beløp

        print()
        print(f"Du satt inn {beløp} kr.")
        print(f"Saldoen er nå {self._saldo} kr")

        return self._saldo

    def ta_ut_beløp(self, beløp: float) -> float:
        if beløp <= 0:
            print()
            print(f"Du prøvde å ta ut {beløp} kr")
            print("Du kan kun ta ut et beløp som er større enn 0 kr")

            return 0

        if self._saldo < beløp:
            print()
            print(f"Du prøver å ta ut {beløp} kr")
            print("Du har ikke nok penger på kontoen")
            print(f"Saldoen er {self._saldo} kr")


            return 0
        
        self._saldo -= beløp

        print()
        print(f"Du tok ut {beløp} kr")
        print(f"Saldoen er nå {self._saldo} kr")

        return beløp
    
    def __str__(self) -> str:
        eier_streng = f"  {"Eier".ljust(11)}: {self._eier}"
        kontonummer_streng = f"  {"Kontonummer".ljust(11)}: {self._kontonummer}"
        saldo_streng = f"  {"Saldo".ljust(11)}: {self._saldo}"

        return "\n".join(["", "Konto:", eier_streng, kontonummer_streng, saldo_streng])



def main() -> None:
    hege = Person("Hege", "Hermansen", "000 00 000")
    konto = Bankkonto(hege, "1820.30.45678")

    konto.motta_beløp(1000)
    konto.motta_beløp(2000)
    konto.ta_ut_beløp(1500)
    konto.ta_ut_beløp(2500)
    konto.ta_ut_beløp(-10)
    konto.motta_beløp(-200)

    print(konto)


if __name__ == "__main__":
    main()
