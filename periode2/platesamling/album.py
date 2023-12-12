from typing import Literal

from person import Artist


class Album:
    def __init__(
        self, navn: str, artist: Artist, plateselskap: str, utgivelsesår: int
    ) -> None:
        self.__navn = navn
        self.__artist = artist
        self.__plateselskap = plateselskap
        self.__utgivelsesår = utgivelsesår

    @property
    def navn(self) -> str:
        return self.__navn

    @property
    def artist(self) -> Artist:
        return self.__artist

    def vis_info(self) -> None:
        print(str(self))

    def __str__(self) -> str:
        return f"Album: {self.__navn}. Laget av: {self.__artist.navn}. Utgitt av {self.__plateselskap} i {self.__utgivelsesår}"


class CD(Album):
    def __str__(self) -> str:
        return super().__str__() + ". Type: CD"


type VinylHastighet = Literal[33, 45]
type FargeRGB = tuple[int, int, int]


class Vinyl(Album):
    def __init__(
        self,
        navn: str,
        artist: Artist,
        plateselskap: str,
        utgivelsesår: int,
        hastighet: VinylHastighet,
        farge: FargeRGB,
    ) -> None:
        super().__init__(navn, artist, plateselskap, utgivelsesår)

        self.__hastighet = hastighet
        self.__farge = farge

    def __str__(self) -> str:
        return (
            super().__str__()
            + f". Type: Vinyl. Hastighet: {self.__hastighet}. Farge: rgb{self.__farge}"
        )
