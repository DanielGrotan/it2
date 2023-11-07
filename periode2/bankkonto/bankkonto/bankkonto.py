from typing import Self

from person import Person


class Bankkonto:
    def __init__(self, eier: Person, kontonummer: str) -> None:
        self.__eier = eier
        self.__kontonummer = kontonummer
        self.__saldo = 0
        
        print("Nyopprettet konto:")
        print(f"  {"Eier".ljust(11)}: {self.__eier}")
        print(f"  {"Kontonummer".ljust(11)}: {self.__kontonummer}")
        print(f"  {"Saldo".ljust(11)}: {self.__saldo}")
    
    @property
    def saldo(self) -> float:
        return self.__saldo

    @classmethod
    def fra_csv(cls, filnavn: str) -> Self:
        with open(filnavn) as f:
            eier_info, kontonummer = f.readline().split(",")
            fornavn, etternavn, telefonnummer = eier_info.split(":")
        
        eier = Person(fornavn, etternavn, telefonnummer)
        return cls(eier, kontonummer)
    
    def motta_beløp(self, beløp: float) -> float:
        if beløp <= 0:
            print()
            print(f"Du prøvde å sette inn {beløp} kr")
            print("Du kan kun sette inn et beløp som er større enn 0 kr")

            return self.__saldo

        self.__saldo += beløp

        print()
        print(f"Du satt inn {beløp} kr.")
        print(f"Saldoen er nå {self.__saldo} kr")

        return self.__saldo

    def ta_ut_beløp(self, beløp: float) -> float:
        if beløp <= 0:
            print()
            print(f"Du prøvde å ta ut {beløp} kr")
            print("Du kan kun ta ut et beløp som er større enn 0 kr")

            return 0

        if self.__saldo < beløp:
            print()
            print(f"Du prøver å ta ut {beløp} kr")
            print("Du har ikke nok penger på kontoen")
            print(f"Saldoen er {self.__saldo} kr")


            return 0
        
        self.__saldo -= beløp

        print()
        print(f"Du tok ut {beløp} kr")
        print(f"Saldoen er nå {self.__saldo} kr")

        return beløp
    
    def __str__(self) -> str:
        eier_streng = f"  {"Eier".ljust(11)}: {self.__eier}"
        kontonummer_streng = f"  {"Kontonummer".ljust(11)}: {self.__kontonummer}"
        saldo_streng = f"  {"Saldo".ljust(11)}: {self.__saldo}"

        return "\n".join(["", "Konto:", eier_streng, kontonummer_streng, saldo_streng])


