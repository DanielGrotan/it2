import random
from typing import Literal, Optional, Self

type Kjønn = Literal["gutt", "jente"]


class Person:
    def __init__(
        self,
        navn: str,
        kjønn: Kjønn,
        minimum_hastighet: float,
        maksimum_hastighet: float,
    ) -> None:
        self.__navn = navn
        self.__kjønn: Kjønn = kjønn
        self.__minimum_hastighet = minimum_hastighet
        self.__maksimum_hastighet = maksimum_hastighet

    def løp(self, distanse: float) -> float:
        hastighet = random.uniform(self.__minimum_hastighet, self.__maksimum_hastighet)

        return distanse / hastighet

    @property
    def navn(self) -> str:
        return self.__navn

    @property
    def kjønn(self) -> Kjønn:
        return self.__kjønn

    @classmethod
    def lag_gutt(cls, navn: str, spesifikk_hastighet: Optional[float] = None) -> Self:
        if spesifikk_hastighet is None:
            return cls(navn, "gutt", 100 / 13, 100 / 11)

        return cls(navn, "gutt", spesifikk_hastighet, spesifikk_hastighet)

    @classmethod
    def lag_jente(cls, navn: str, spesifikk_hastighet: Optional[float] = None) -> Self:
        if spesifikk_hastighet is None:
            return Person(navn, "jente", 100 / 13.5, 100 / 11.5)

        return Person(navn, "jente", spesifikk_hastighet, spesifikk_hastighet)
