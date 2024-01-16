import numpy as np
from matplotlib import pyplot as plt


def main() -> None:
    data = {
        1985: [71, 50],
        1989: [63, 37],
        1993: [67, 28],
        1997: [65, 23],
        2001: [43, 38],
        2005: [61, 38],
        2009: [64, 41],
        2013: [55, 48],
        2017: [49, 45],
        2021: [48, 36],
    }

    years = np.array([1985, 1989, 1993, 1997, 2001, 2005, 2009, 2013, 2017, 2021])
    ap_votes = [71, 63, 67, 65, 43, 61, 64, 55, 49, 48]
    h_votes = [50, 37, 28, 23, 38, 38, 41, 48, 45, 36]

    plt.bar(years + 0.5, ap_votes, width=1, label="Arbeiderpartiet", color="red")
    plt.bar(years - 0.5, h_votes, width=1, label="Høyre", color="blue")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
