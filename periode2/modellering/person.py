class Person:
    def __init__(self, fornavn: str, etternavn: str, telefonnummer: str) -> None:
        self._fornavn = fornavn
        self._etternavn = etternavn
        self._telefonnummer = telefonnummer

    def hent_fornavn(self) -> str:
        return self._fornavn

    def hent_etternavn(self) -> str:
        return self._etternavn

    def hent_telefonnummer(self) -> str:
        return self._telefonnummer
