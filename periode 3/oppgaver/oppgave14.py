import numpy as np
from matplotlib import patches as mpatches
from matplotlib import pyplot as plt


def main() -> None:
    programs = [
        "Bygg- og anleggsteknikk",
        "Elektro og datateknologi",
        "Helse- og oppvekstfag",
        "Naturbruk",
        "Restaurant- og matfag",
        "Teknologi- og industrifag",
        "Håndverk, design og produktutvikling",
        "Frisør, blomster, interiør og eksponeringsdesign",
        "Informasjonsteknologi og medieproduksjon",
        "Salg, service og reiseliv",
    ]

    counts = np.array(
        [
            [3811, 352],
            [4168, 268],
            [8661, 7286],
            [2057, 1028],
            [1484, 709],
            [5501, 851],
            [313, 243],
            [901, 826],
            [1309, 200],
            [2061, 895],
        ]
    )

    fig, ax = plt.subplots()

    ax.pie(
        counts.sum(axis=1),
        radius=1,
        wedgeprops=dict(width=0.3, edgecolor="w"),
        labels=programs,
    )
    ax.pie(
        counts.flatten(),
        radius=1 - 0.3,
        colors=["blue", "pink"],
        wedgeprops=dict(width=0.3, edgecolor="w"),
    )

    ax.set(aspect="equal")

    blue_patch = mpatches.Patch(color="blue", label="Gutter")
    pink_patch = mpatches.Patch(color="pink", label="Jenter")

    ax.legend(loc="upper right", handles=[blue_patch, pink_patch])

    plt.show()


if __name__ == "__main__":
    main()
