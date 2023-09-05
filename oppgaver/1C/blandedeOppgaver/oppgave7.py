def fibonacci(n: int) -> int:
    if n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def main() -> None:
    fibonacci_numbers = (fibonacci(n) for n in range(1, 8))

    print(f"De 7 første fibonaccitallene er: {', '.join(map(str, fibonacci_numbers))}")


if __name__ == "__main__":
    main()
