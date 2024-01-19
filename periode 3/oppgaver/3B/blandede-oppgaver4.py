import os

import pandas
from matplotlib import pyplot as plt

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "datafiler")


def main() -> None:
    df = pandas.read_csv(
        os.path.join(DATA_DIR, "timetrafikk2.csv"), delimiter=";", encoding="utf-8"
    )

    total_trafic_index = df["Felt"] == "Totalt"
    total_trafic_rows = df[total_trafic_index]

    plt.bar(total_trafic_rows["Fra tidspunkt"], total_trafic_rows["Trafikkmengde"])

    plt.xlabel("Tidspunkt (starttid)")
    plt.ylabel("Trafikkmengde")

    plt.title("Trafikkmengde ved dragveien på ulike tidspunkt")

    plt.show()


if __name__ == "__main__":
    main()
