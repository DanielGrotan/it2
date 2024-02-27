import csv
import math
import os

import numpy as np
from matplotlib import pyplot as plt

ABSOLUTE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def get_absolute_path(relative_path: str) -> str:
    return os.path.join(ABSOLUTE_DIR_PATH, relative_path)


def read_and_clean_data() -> tuple[list[str], list[list[str | float]]]:
    with open(get_absolute_path("datasett/Medier.csv"), encoding="utf-8") as f:
        csv_reader = csv.reader(f, delimiter=";")

        # skip the first 2 lines
        next(csv_reader)
        next(csv_reader)

        # shorten the headers
        headers = next(csv_reader)
        headers[1:] = [header.split(" ")[-1] for header in headers[1:]]
        years = headers[1:]

        rows: list[list[str | float]] = list(csv_reader)  # type: ignore

    for row in rows:
        for j, cell in enumerate(row[1:]):
            if cell == "." or cell == "..":
                row[j + 1] = np.NaN
                continue

            row[j + 1] = int(cell)

    return years, rows


def decorate_graph() -> None:
    plt.title("Tid brukt til ulike medier en gjennomsnittsdag (minutter)")
    plt.xlabel("År")
    plt.ylabel("Tid brukt (minutter)")
    plt.legend()


def plot_all_data(years: list[str], rows: list[list[str | float]]) -> None:
    for media_type, *counts in rows:
        plt.plot(years, counts, label=media_type)

    decorate_graph()
    plt.show()


def plot_specific_media_types(
    media_types: set[str], years: list[str], rows: list[list[str | float]]
) -> None:
    for media_type, *counts in rows:
        if media_type not in media_types:
            continue

        plt.plot(years, counts, label=media_type)

    decorate_graph()
    plt.savefig(get_absolute_path("out/oppgave1b.png"))


def print_lowest_and_highest_count(
    target_media_type: str, years: list[str], rows: list[list[str | float]]
) -> None:
    media_type_index = -1

    for i, (media_type, *_) in enumerate(rows):
        if media_type == target_media_type:
            media_type_index = i
            break

    assert media_type_index != -1, f"Finner ikke {target_media_type} i datasettet"

    _, *counts = rows[media_type_index]

    lowest_count = math.inf
    lowest_count_year = None

    highest_count = -math.inf
    highest_count_year = None

    for year, count in zip(years, counts):
        if count < lowest_count:
            lowest_count = count
            lowest_count_year = year

        if count > highest_count:
            highest_count = count
            highest_count_year = year

    print(
        f"Internettbruken var lavest i {lowest_count_year} med {lowest_count} daglig gjennomsnitt og høyest i {highest_count_year} med {highest_count} daglig gjennomsnitt"
    )


def main() -> None:
    years, rows = read_and_clean_data()

    plot_all_data(years, rows)
    plot_specific_media_types({"Hjemme-PC", "Bøker", "Internett"}, years, rows)

    print_lowest_and_highest_count("Internett", years, rows)


if __name__ == "__main__":
    main()
