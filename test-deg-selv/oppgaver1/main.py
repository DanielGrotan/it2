from typing import Callable, Literal, TypedDict


class Oppskrift(TypedDict):
    sukker: float
    mel: float
    smør: float


def oppskrift_fra_sukker(gram_sukker: float) -> Oppskrift:
    return {"sukker": gram_sukker, "mel": gram_sukker * 2, "smør": gram_sukker * 3}


def oppskrift_fra_mel(gram_mel: float) -> Oppskrift:
    return {"sukker": gram_mel / 2, "mel": gram_mel, "smør": gram_mel / 2 * 3}


def oppskrift_fra_smør(gram_smør: float) -> Oppskrift:
    return {"sukker": gram_smør / 3, "mel": gram_smør / 3 * 2, "smør": gram_smør}


OPPSKRIFT_FRA_INGREDIENS: dict[str, Callable[[float], Oppskrift]] = {
    "sukker": oppskrift_fra_sukker,
    "mel": oppskrift_fra_mel,
    "smør": oppskrift_fra_smør,
}


def skriv_oppskrift(gram_sukker: float, gram_mel: float, gram_smør: float) -> None:
    print("Oppskrift på kaker")
    print("Du trenger:")
    print(f"{gram_sukker} gram sukker")
    print(f"{gram_mel} gram mel")
    print(f"{gram_smør} gram smør")


def spør_bruker_om_ingrediens() -> str:
    gyldige_ingredienser = {"sukker", "mel", "smør"}

    while True:
        ingrediens = input(
            "Hvilken ingrediens vil du ta utgangspunkt i (sukker/mel/smør)? "
        ).lower()

        if ingrediens in gyldige_ingredienser:
            return ingrediens

        print("Ugyldig ingrediens. Prøv på nytt")


def spør_bruker_om_antall_gram(ingrediens: str) -> float:
    while True:
        try:
            antall_gram = float(
                input(f"Hvor mye {ingrediens} har du (oppgitt i gram)? ")
            )
            return antall_gram
        except ValueError:
            print("Du må skrive et tall")


def bak_kaker() -> None:
    ingrediens = spør_bruker_om_ingrediens()
    gram_ingrediens = spør_bruker_om_antall_gram(ingrediens)
    oppskrift = OPPSKRIFT_FRA_INGREDIENS[ingrediens](gram_ingrediens)

    skriv_oppskrift(oppskrift["sukker"], oppskrift["mel"], oppskrift["smør"])


def tester() -> None:
    sukker_verdier = [0, 1, 4, 2.3, 5.66]

    for gram_sukker in sukker_verdier:
        print(f"\nTester med {gram_sukker=}")

        oppskrift = oppskrift_fra_sukker(gram_sukker)

        skriv_oppskrift(oppskrift["sukker"], oppskrift["mel"], oppskrift["smør"])


def main() -> None:
    kjør_tester = False

    if kjør_tester:
        tester()

    bak_kaker()


if __name__ == "__main__":
    main()
