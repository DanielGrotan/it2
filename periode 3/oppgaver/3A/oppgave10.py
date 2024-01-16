# kopiert fra oppgave 8
from dataclasses import dataclass

from matplotlib import pyplot as plt


@dataclass
class CarProduction:
    country: str
    cars_produced: int


def format_car_productions(
    car_productions: list[CarProduction],
) -> tuple[list[str], list[int]]:
    sorted_productions = sorted(
        car_productions, key=lambda car_production: car_production.country, reverse=True
    )

    country_names = [car_production.country for car_production in sorted_productions]
    cars_produced = [
        car_production.cars_produced for car_production in sorted_productions
    ]

    return country_names, cars_produced


def plot_car_productions(country_names: list[str], cars_produced: list[int]) -> None:
    plt.barh(country_names, cars_produced, color="hotpink", height=0.3)  # type: ignore

    plt.title("Top 10 countries by car production")
    plt.xlabel("Cars produced")
    plt.subplots_adjust(left=0.2)

    plt.show()


def main() -> None:
    car_productions = [
        CarProduction("China", 24_420_744),
        CarProduction("Japan", 7_873_886),
        CarProduction("Germany", 5_746_808),
        CarProduction("USA", 3_934_357),
        CarProduction("South Korea", 3_859_991),
        CarProduction("India", 3_677_605),
        CarProduction("Spain", 2_354_117),
        CarProduction("Mexico", 1_993_168),
        CarProduction("Brazil", 1_778_464),
        CarProduction("UK", 1_722_698),
    ]

    formatted_productions = format_car_productions(car_productions)
    plot_car_productions(*formatted_productions)


if __name__ == "__main__":
    main()
