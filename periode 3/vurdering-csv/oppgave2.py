import os

import pandas as pd
from matplotlib import pyplot as plt

ABSOLUTE_DIR_PATH = os.path.dirname(os.path.abspath(__file__))


def get_absolute_path(relative_path: str) -> str:
    return os.path.join(ABSOLUTE_DIR_PATH, relative_path)


def load_and_clean_data() -> pd.DataFrame:
    df = pd.read_csv(
        get_absolute_path("datasett/Medier.csv"),
        index_col=0,
        skiprows=(0, 1),
        sep=";",
        na_values=[".", ".."],
        encoding="utf-8",
    )

    df.columns = df.columns.map(lambda column: column.split(" ")[-1])

    return df


def decorate_graph() -> None:
    plt.title("Tid brukt til ulike medier en gjennomsnittsdag (minutter)")
    plt.xlabel("År")
    plt.ylabel("Tid brukt (minutter)")
    plt.legend()


def plot_all_data(df: pd.DataFrame) -> None:
    df.T.plot()
    decorate_graph()
    plt.show()


def plot_specific_media_types(media_types: list[str], df: pd.DataFrame) -> None:
    df.loc[media_types].T.plot()
    decorate_graph()
    plt.savefig(get_absolute_path("out/oppgave2b.png"))


def print_lowest_and_highest_count(media_type: str, df: pd.DataFrame) -> None:
    row = df.loc[media_type]

    print(
        f"Internettbruken var lavest i {row.idxmin()} med {row.min()} daglig gjennomsnitt og høyest i {row.idxmax()} med {row.max()} daglig gjennomsnitt"
    )


def main() -> None:
    df = load_and_clean_data()

    plot_all_data(df)
    plot_specific_media_types(["Hjemme-PC", "Bøker", "Internett"], df)

    print_lowest_and_highest_count("Internett", df)


if __name__ == "__main__":
    main()
