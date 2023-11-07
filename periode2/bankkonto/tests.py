from bankkonto import Bankkonto, BSUKonto, Sparekonto
from person import Person


def test_bankkonto() -> None:
    hege = Person("Hege", "Hermansen", "000 00 000")
    konto = Bankkonto(hege, "1820.30.45678")
    assert konto.saldo == 0, "Saldoen ble ikke satt til 0 ved opprettelse"

    konto.motta_beløp(1000)
    assert konto.saldo == 1000, "Saldoen er feil"

    konto.motta_beløp(2000)
    assert konto.saldo == 3000, "Saldoen er feil"

    konto.ta_ut_beløp(1500)
    assert konto.saldo == 1500, "Saldoen er feil"

    konto.ta_ut_beløp(2500)
    assert konto.saldo == 1500, "Burde ikke kunne ta ut mer penger"

    konto.ta_ut_beløp(-10)
    assert konto.saldo == 1500, "Kan ikke ta ut negativt beløp"

    konto.motta_beløp(-200)
    assert konto.saldo == 1500, "Kan ikke sette inn negativt"


def test_bsu_konto() -> None:
    person = Person("Hege", "Hermansen", "000 00 000")
    konto = BSUKonto(person, "1983918291", 4000)
    assert konto.saldo == 0, "Saldoen ble ikke satt til 0 ved opprettelse"

    konto.motta_beløp(3000)
    assert konto.saldo == 3000, "Saldoen er feil"

    konto.motta_beløp(2000)
    assert konto.saldo == 3000, "Beløpet går over overskuddet"

    konto.motta_beløp(1000)
    assert konto.saldo == 4000, "Saldoen er feil"

    konto.motta_beløp(300)
    assert konto.saldo == 4000, "Beløpet går over overskuddet"


def test_sparekonto() -> None:
    person = Person("Hege", "Hermansen", "000 00 000")
    konto = Sparekonto(person, "173873283", 3)
    assert konto.saldo == 0, "Saldoen ble ikke satt til 0 ved opprettelse"

    konto.motta_beløp(2000)
    assert konto.saldo == 2000, "Saldoen er feil"

    konto.ta_ut_beløp(100)
    assert konto.saldo == 1900, "Saldoen er feil"

    konto.ta_ut_beløp(100)
    assert konto.saldo == 1800, "Saldoen er feil"

    konto.ta_ut_beløp(100)
    assert konto.saldo == 1700, "Saldoen er feil"

    konto.ta_ut_beløp(200)
    assert konto.saldo == 1700, "Kan ikke ta ut mer penger"


if __name__ == "__main__":
    test_bankkonto()
    test_bsu_konto()
    test_sparekonto()
