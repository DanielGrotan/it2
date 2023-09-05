def main() -> None:
    numbers = [70, 9, 8, 7, 6, 5, 4, 3, 2, 100]

    numbers.pop()
    numbers.insert(0, 10)
    numbers.remove(70)
    numbers.append(1)
    numbers.reverse()

    print(numbers)


if __name__ == "__main__":
    main()
