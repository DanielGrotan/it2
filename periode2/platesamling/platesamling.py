from typing import Optional

from album import Album
from person import Artist, Eier


class Platesamling:
    def __init__(self, eier: Eier) -> None:
        self.__eier = eier
        self.__album: dict[str, list[Album]] = {}

    def legg_til_album(self, album: Album) -> None:
        artist = album.artist
        self.legg_til_artist(artist)

        self.__album[artist.navn].append(album)

    def legg_til_artist(self, artist: Artist) -> None:
        if artist.navn not in self.__album:
            self.__album[artist.navn] = []

    def vis_album_navn(self, artist: Optional[Artist] = None) -> None:
        if artist is not None:
            album = (
                enkelt_album.navn
                for enkelt_album in self.__album.get(artist.navn) or []
            )
        else:
            album = (
                enkelt_album.navn
                for album in self.__album.values()
                for enkelt_album in album
            )

        print(f"Albumnavn i platesamlingen: {", ".join(album)}")

    def vis_artister(self) -> None:
        if len(self.__album) == 0:
            print("Platesamlingen har ingen artister")
            return

        print(f"Artister: {", ".join(self.__album)}")
    
    def vis_info(self) -> None:
        print(str(self))
    
    def __str__(self) -> str:
        return f"Eier: {self.__eier}\nAntall album per artist:\n{"\n".join(f"{artist_navn}: {len(album)}" for artist_navn, album in self.__album.items())}"
