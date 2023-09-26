import math


def print_countries(country_to_population: dict[str, int]) -> None:
    print(
        f"The top 5 most populous countires in the world are: {', '.join(country_to_population.keys())}"
    )


def print_populations(country_to_population: dict[str, int]) -> None:
    print(
        f"The populations are: {', '.join(str(population) for population in country_to_population.values())}"
    )


def print_countries_with_populations(country_to_population: dict[str, int]) -> None:
    for country, population in country_to_population.items():
        print(f"{country} has {population} citizens")


def print_countries_sorted_alphabetically(
    country_to_population: dict[str, int]
) -> None:
    print(", ".join(sorted(country_to_population.keys())))


def print_min_max_populations(country_to_population: dict[str, int]) -> None:
    smallest_population = (math.inf, None)
    largest_population = (-math.inf, None)

    for country, population in country_to_population.items():
        if population < smallest_population[0]:
            smallest_population = (population, country)

        if population > largest_population[0]:
            largest_population = (population, country)

    print(
        f"{largest_population[1]} has the largest population. {smallest_population[1]} has the smallest population"
    )


def main() -> None:
    country_to_population: dict[str, int] = {
        "India": int(1_425.8 * 10**6),
        "China": int(1_425.7 * 10**6),
        "USA": int(333.3 * 10**6),
        "Indonesia": int(275.5 * 10**6),
        "Pakistan": int(235.8 * 10**6),
    }

    print_countries(country_to_population)
    print_populations(country_to_population)
    print_countries_with_populations(country_to_population)
    print_countries_sorted_alphabetically(country_to_population)
    print_min_max_populations(country_to_population)


if __name__ == "__main__":
    main()
