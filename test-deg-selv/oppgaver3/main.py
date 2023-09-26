import math

PRISLISTE = [
    {"salat": 12, "fisk": 99, "melk": 12, "brod": 12},
    {"salat": 22, "fisk": 60, "melk": 18, "brod": 21},
    {"salat": 8, "fisk": 120, "melk": 10, "brod": 19},
    {"salat": 18, "fisk": 40, "melk": 30, "brod": 59},
    {"salat": 15, "fisk": 200, "melk": 40, "brod": 9},
]

BUTIKKER = ["Rema1000", "Meny", "Kiwi", "Spar", "Joker"]


def finn_butikk(
    handleliste: list[str], prisliste: list[dict[str, int]], butikker: list[str]
) -> str:
    total_priser = [0] * len(butikker)

    for vare in handleliste:
        for i, priser in enumerate(prisliste):
            total_priser[i] += priser[vare]

    lavest_pris = math.inf
    lavest_pris_butikk_indeks = -1

    for i, pris in enumerate(total_priser):
        if pris < lavest_pris:
            lavest_pris = pris
            lavest_pris_butikk_indeks = i

    return butikker[lavest_pris_butikk_indeks]


print(finn_butikk(["salat", "melk"], PRISLISTE, BUTIKKER))
