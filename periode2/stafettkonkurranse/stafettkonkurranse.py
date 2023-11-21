from lag import Lag


class Stafettkonkurranse:
    def __init__(self, lag: list[Lag], distanse: float) -> None:
        self.__lag = lag
        self.__distanse = distanse

    def konkurrer(self, antall_runder: int) -> None:
        totaltider = [0.0 for _ in range(len(self.__lag))]

        for runde in range(1, antall_runder + 1):
            print(f"\nRunde {runde}:")

            for i, lag in enumerate(self.__lag):
                print(f"\nLag {i + 1}:")
                tider = lag.gjennomfør_løp(self.__distanse)

                totaltid = sum(tider)
                totaltider[i] += totaltid

        sorterte_tider = list(
            sorted(enumerate(totaltider), key=lambda indeks_tid_par: indeks_tid_par[1])
        )

        print("\nTotaltider:")
        for indeks, tid in sorterte_tider:
            print(f"Lag {indeks + 1}. Total tid: {tid:.2f} s")
