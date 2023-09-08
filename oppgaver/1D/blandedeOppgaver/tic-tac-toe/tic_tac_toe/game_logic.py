from typing import Any, Callable, Generator, Iterable, TypeVar

from tic_tac_toe.types import Board, PlayerSymbol


def _count_consecutive(
    board: Board, symbol: PlayerSymbol, rows: Iterable[int], cols: Iterable[int]
) -> int:
    consecutive = 0

    for row, col in zip(rows, cols):
        if board[row][col] != symbol:
            break

        consecutive += 1

    return consecutive


T = TypeVar("T")


def _value_as_infinite_generator(value: T) -> Generator[T, Any, None]:
    while True:
        yield value


def check_for_winner(
    board: Board,
    player_symbol: PlayerSymbol,
    updated_row: int,
    updated_col: int,
    consecutive_to_win: int,
) -> bool:
    decreasing_iterable: Callable[[int], Iterable[int]] = lambda base_value: range(
        base_value - 1, max(-1, base_value - consecutive_to_win), -1
    )
    increasing_iterable: Callable[[int], Iterable[int]] = lambda base_value: range(
        base_value + 1, min(len(board[0]), base_value + consecutive_to_win)
    )
    static_iterable: Callable[
        [int], Iterable[int]
    ] = lambda base_value: _value_as_infinite_generator(base_value)

    row_moving_up = lambda: decreasing_iterable(updated_row)
    row_moving_down = lambda: increasing_iterable(updated_row)
    row_not_moving = lambda: static_iterable(updated_row)

    col_moving_left = lambda: decreasing_iterable(updated_col)
    col_moving_right = lambda: increasing_iterable(updated_col)
    col_not_moving = lambda: static_iterable(updated_col)

    win_condition_pairs = [
        # left to right
        (
            (row_not_moving(), col_moving_left()),
            (row_not_moving(), col_moving_right()),
        ),
        # up to down
        (
            (row_moving_up(), col_not_moving()),
            (row_moving_down(), col_not_moving()),
        ),
        # top left to bottom right
        (
            (row_moving_up(), col_moving_left()),
            (row_moving_down(), col_moving_right()),
        ),
        # top right to bottom left
        (
            (row_moving_up(), col_moving_right()),
            (row_moving_down(), col_moving_left()),
        ),
    ]

    for first_part, second_part in win_condition_pairs:
        consecutive = _count_consecutive(board, player_symbol, *first_part)

        if consecutive + 1 >= consecutive_to_win:
            return True

        consecutive += _count_consecutive(board, player_symbol, *second_part)

        if consecutive + 1 >= consecutive_to_win:
            return True

    return False
