from album import CD, Vinyl
from person import Artist, Eier
from platesamling import Platesamling


def main() -> None:
    eier = Eier("Daniel")
    platesamling = Platesamling(eier)

    david_bowie = Artist("David Bowie")
    best_of_bowie = CD("Best Of Bowie", david_bowie, "Parlophone UK", 2002)

    print(best_of_bowie)
    print()

    platesamling.legg_til_album(best_of_bowie)

    platesamling.vis_artister()
    platesamling.vis_album_navn()
    print()

    justin_bieber = Artist("Justin Bieber")
    platesamling.legg_til_artist(justin_bieber)

    platesamling.vis_artister()
    platesamling.vis_album_navn()
    print()

    print(platesamling)


if __name__ == "__main__":
    main()
