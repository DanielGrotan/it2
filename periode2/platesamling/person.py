class Person:
    def __init__(self, navn: str) -> None:
        self.__navn = navn

    @property
    def navn(self) -> str:
        return self.__navn

    def __str__(self) -> str:
        return self.__navn


class Eier(Person):
    pass


class Artist(Person):
    pass
