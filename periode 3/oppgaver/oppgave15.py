from matplotlib import pyplot as plt


def main() -> None:
    time = {
        "Sove": 8,
        "Gå til/fra skolen": 1.5,
        "Skole": 7 + 1 / 3,
        "Spise mat": 1,
        "Slappe av": 24 - (8 + 1.5 + 7 + 1 / 3 + 1),
    }

    plt.pie(time.values(), labels=time.keys())
    plt.show()


if __name__ == "__main__":
    main()
