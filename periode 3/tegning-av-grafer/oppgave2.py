import os
import random

from matplotlib import pyplot as plt


def plot_dice_throws(n_throws: int, output_path: str | None = None) -> None:
    throw_results = [0] * 6

    for _ in range(n_throws):
        dice_throw = random.randint(1, 6)
        throw_results[dice_throw - 1] += 1

    plt.scatter(range(1, 7), throw_results)

    plt.title("Antall terningkast med ulike antall øyne")
    plt.ylabel("Antall kast")
    plt.xlabel("Antall øyne")

    if output_path is not None:
        plt.savefig(output_path)

    plt.show()


def main() -> None:
    OUTPUT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "output")

    plot_dice_throws(100, output_path=os.path.join(OUTPUT_DIR, "2a.png"))
    plot_dice_throws(100000, output_path=os.path.join(OUTPUT_DIR, "2c.png"))


if __name__ == "__main__":
    main()
