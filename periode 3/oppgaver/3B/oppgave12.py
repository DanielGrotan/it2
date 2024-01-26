import json
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


def get_absolute_path(relative_path: str) -> str:
    return os.path.join(ROOT_PATH, relative_path)


def print_countries(data) -> None:
    get_country_name = lambda country: country["navn"]

    country_names = ", ".join(map(get_country_name, data["land"]))

    print(f"Landene er: {country_names}")


def print_denmark_cities(data) -> None:
    country_is_denmark = lambda country: country["navn"] == "Danmark"

    denmark = next(filter(country_is_denmark, data["land"]))

    city_names = ", ".join(denmark["byer"])

    print(f"Byene i danmark er: {city_names}")

def print_countries_and_cities(data) -> None:
    countries = data["land"]

    for country in countries:
        print()
        print(f"Land: {country["navn"]}")
        print(f"Byer: {", ".join(country["byer"])}")

def print_denmark_cities_starting_with_a(data) -> None:
    country_is_denmark = lambda country: country["navn"] == "Danmark"
    denmark = next(filter(country_is_denmark, data["land"]))

    city_name_starts_with_a = lambda city_name: city_name.startswith("A")

    city_names = ", ".join(filter(city_name_starts_with_a, denmark["byer"]))

    print(f"Byer i Danmark som starter med 'A': {city_names}")


def main() -> None:
    with open(get_absolute_path("datafiler/skandinavia.json"), encoding="utf-8") as f:
        data = json.load(f)

    print_countries(data)
    print_denmark_cities(data)
    print_countries_and_cities(data)
    print_denmark_cities_starting_with_a(data)


if __name__ == "__main__":
    main()
