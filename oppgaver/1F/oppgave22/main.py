import lib


def main() -> None:
    while True:
        command = input(
            "Enter command (sum, average, first_number, smallest_number, quit): "
        )

        function = None
        match command.lower():
            case "quit":
                break
            case "sum":
                function = lib.sum_numbers
            case "average":
                function = lib.average
            case "first_number":
                function = lib.first_number
            case "smallest_number":
                function = lib.smallest_number
            case _:
                print("Invalid command. Try again")
                continue

        try:
            numbers = list(
                int(number)
                for number in input(
                    "Enter the numbers you want to call the function on (1, 2, 3): "
                ).split(", ")
            )
        except ValueError:
            print("Invalid input. Try again")
            continue

        if not numbers:
            print("Invalid input. Try agsin")
            continue

        print(f"Result: {function(numbers)}")


if __name__ == "__main__":
    main()
