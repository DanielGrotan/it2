from typing import Any, Callable


def sum_numbers(numbers: list[int]) -> int:
    sum_ = 0

    for number in numbers:
        sum_ += number

    return sum_


def average(numbers: list[int]) -> float:
    if not numbers:
        raise ValueError("Can't find average of an empty list")

    return sum_numbers(numbers) / len(numbers)


def first_number(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError("Can't find first number of an empty list")

    return numbers[0]


def smallest_number(numbers: list[int]) -> int:
    if not numbers:
        raise ValueError("Can't find smallest number of an empty list")

    return min(numbers)


def _assert_raises(
    condition: Callable[[], Any], error_type: type, error_message: str
) -> None:
    try:
        condition()
    except Exception as e:
        if isinstance(e, error_type):
            return

    raise AssertionError(error_message)


def _test_sum_numbers():
    assert sum_numbers([1, 2, 4]) == 7
    assert sum_numbers([]) == 0
    assert sum_numbers([-1, 6]) == 5


def _test_average():
    assert average([1, 1]) == 1
    assert average([2, -2]) == 0

    _assert_raises(
        lambda: average([]),
        ValueError,
        "average function should raise a ValueError if an empty list is passed",
    )


def _test_first_number():
    assert first_number([1, 2, 3]) == 1
    assert first_number([-10, 489, 33]) == -10

    _assert_raises(
        lambda: first_number([]),
        ValueError,
        "first_number function should raise a ValueError if an empty list is passed",
    )


def _test_smallest_number():
    assert smallest_number([3, 2, 1]) == 1
    assert smallest_number([-32, -4, 3, -44, 378]) == -44

    _assert_raises(
        lambda: smallest_number([]),
        ValueError,
        "smallest_number function should raise a ValueError if an empty list is passed",
    )


def main() -> None:
    _test_sum_numbers()
    _test_average()
    _test_first_number()


if __name__ == "__main__":
    main()
