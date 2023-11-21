import tester
from idrettslag import Idrettslag
from person import Person
from stafettkonkurranse import Stafettkonkurranse


def main() -> None:
    idrettslag = Idrettslag()

    gutter = [Person.lag_gutt(f"Gutt {i}") for i in range(1, 5)] + [
        Person.lag_gutt("Spesiell gutt", 10)
    ]
    jenter = [Person.lag_jente(f"Jente {i}") for i in range(1, 5)] + [
        Person.lag_jente("Spesiell jente", 10)
    ]

    idrettslag.legg_til_medlemer(*gutter, *jenter)

    lag = idrettslag.trekk_lag(2, 2)

    stafettkonkurranse = Stafettkonkurranse(lag, 100)
    stafettkonkurranse.konkurrer(2)


if __name__ == "__main__":
    # tester.kjør_tester()
    main()
