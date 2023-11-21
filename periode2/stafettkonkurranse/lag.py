from person import Person


class Lag:
    def __init__(self, medlemmer: list[Person]):
        self.__medlemmer = medlemmer

    @property
    def medlemmer(self) -> list[Person]:
        return self.__medlemmer[:]

    def gjennomfør_løp(self, distanse: float) -> list[float]:
        konkurransetider = []

        for medlem in self.__medlemmer:
            tid = medlem.løp(distanse)

            print(f"{medlem.navn} løp på {tid:.2f} s")

            konkurransetider.append(medlem.løp(distanse))

        return konkurransetider

    def __str__(self) -> str:
        return ", ".join(map(str, self.__medlemmer))
