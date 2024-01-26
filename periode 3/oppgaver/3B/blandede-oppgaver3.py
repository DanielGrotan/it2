import os

from matplotlib import pyplot as plt

ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT_DIR, "datafiler")


def task_a() -> dict[str, list[str] | list[int]]:
    data = {}

    with open(
        os.path.join(DATA_DIR, "fritidsboliger_moh_2019.csv"), encoding="utf-8-sig"
    ) as f:
        for line in f:
            column_name, *row_values = line.strip().split(";")
            data[column_name] = row_values

    data["Fritidsbygg"] = [int(value) for value in data["Fritidsbygg"]]

    return data


def task_b(data: dict[str, list[str] | list[int]]) -> None:
    plt.barh(data["Meter over havet"], data["Fritidsbygg"])

    plt.title("Fordeling av fritidsbygg over høyde over havet")

    plt.xlabel("Antall fritidsbygg")
    plt.ylabel("Meter over havet")

    plt.show()


def task_c(data: dict[str, list[str] | list[int]]) -> None:
    sum_over_1000 = sum(data["Fritidsbygg"][13:])

    print(sum_over_1000)

    data["Meter over havet"] = data["Meter over havet"][:13] + ["Over 1000 m"]
    data["Fritidsbygg"] = data["Fritidsbygg"][:13] + [sum_over_1000]

    task_b(data)


def main() -> None:
    data = task_a()
    task_b(data)
    task_c(data)


if __name__ == "__main__":
    main()
