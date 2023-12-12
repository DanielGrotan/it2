import os

import matplotlib.pyplot as plt
import numpy as np

OUTPUT_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "output")


def task_a() -> None:
    x = np.linspace(-2, 2, 1000)

    functions = [lambda x: x**3, lambda x: 3 * x**2, lambda x: 6 * x]
    function_names = ["f(x)", "f'(x)", "f''(x)"]
    function_expressions = ["x^3", "3x^2", "6x"]
    colors = ["r", "g", "b"]

    for function, name, expression, color in zip(
        functions, function_names, function_expressions, colors
    ):
        plt.plot(x, function(x), color, label=f"${name} = {expression}$")

    plt.legend()
    plt.grid()
    plt.title("Grafene til $f(x)$, $f'(x)$ og $f''(x)$")

    plt.savefig(os.path.join(OUTPUT_DIR, "1a.png"))
    plt.show()


def task_b() -> None:
    x = np.linspace(-2, 2, 1000)

    functions = [lambda x: x**3, lambda x: 3 * x**2, lambda x: 6 * x]
    function_names = ["f(x)", "f'(x)", "f''(x)"]
    function_expressions = ["x^3", "3x^2", "6x"]
    colors = ["r", "g", "b"]

    fig, axs = plt.subplots(3, 1)

    fig.suptitle("$f(x)$, $f'(x)$ og $f''(x)$")

    for ax, function, name, expression, color in zip(
        axs, functions, function_names, function_expressions, colors
    ):
        ax.set_title(f"Grafen til ${name}$")
        ax.plot(x, function(x), color, label=f"${name} = {expression}$")
        ax.legend()

    fig.subplots_adjust(hspace=1)

    fig.savefig(os.path.join(OUTPUT_DIR, "1b.png"))
    plt.show()


def main() -> None:
    if not os.path.isdir(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    task_a()
    task_b()


if __name__ == "__main__":
    main()
