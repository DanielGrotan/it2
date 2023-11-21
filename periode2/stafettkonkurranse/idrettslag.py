import random

from lag import Lag
from person import Person


class Idrettslag:
    def __init__(self):
        self.__gutter: list[Person] = []
        self.__jenter: list[Person] = []

    @property
    def gutter(self) -> list[Person]:
        return self.__gutter[:]

    @property
    def jenter(self) -> list[Person]:
        return self.__jenter[:]

    def legg_til_medlemer(self, *personer: Person) -> None:
        for person in personer:
            if person.kjønn == "gutt":
                self.__gutter.append(person)
            elif person.kjønn == "jente":
                self.__jenter.append(person)

    def trekk_lag(self, gutter_per_lag: int, jenter_per_lag: int) -> list[Lag]:
        gutter_kopi = list(self.__gutter)
        random.shuffle(gutter_kopi)

        jenter_kopi = list(self.__jenter)
        random.shuffle(jenter_kopi)

        gutter_indeks = 0
        jenter_indeks = 0

        lag: list[Lag] = []

        while gutter_indeks + gutter_per_lag <= len(
            gutter_kopi
        ) and jenter_indeks + jenter_per_lag <= len(jenter_kopi):
            gutter = gutter_kopi[gutter_indeks : gutter_indeks + gutter_per_lag]
            gutter_indeks += gutter_per_lag

            jenter = jenter_kopi[jenter_indeks : jenter_indeks + jenter_per_lag]
            jenter_indeks += jenter_per_lag

            lag.append(Lag(gutter + jenter))

        return lag
