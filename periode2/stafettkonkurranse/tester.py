from idrettslag import Idrettslag
from person import Person


def kjør_tester():
    idrettslag = Idrettslag()

    gutter = [Person.lag_gutt(f"Gutt {i}") for i in range(1, 5)] + [
        Person.lag_gutt("Spesiell gutt", 10)
    ]
    jenter = [Person.lag_jente(f"Jente {i}") for i in range(1, 5)] + [
        Person.lag_jente("Spesiell jente", 10)
    ]

    idrettslag.legg_til_medlemer(*gutter, *jenter)

    assert len(idrettslag.gutter) == 5
    assert len(idrettslag.jenter) == 5

    lag = idrettslag.trekk_lag(2, 2)

    assert len(lag) == 2

    antall_gutter = len(
        list(filter(lambda person: person.kjønn == "gutt", lag[0].medlemmer))
    )
    antall_jenter = len(
        list(filter(lambda person: person.kjønn == "jente", lag[0].medlemmer))
    )

    assert antall_gutter == 2
    assert antall_jenter == 2
