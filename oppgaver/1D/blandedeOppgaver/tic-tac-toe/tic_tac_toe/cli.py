import re

from tic_tac_toe.constants import EMPTY_SYMBOL
from tic_tac_toe.types import Board

SQUARE_DIMENSIONS_REGEX = re.compile(r"[1-9]\d*")
RECTANGULAR_DIMENSIONS_REGEX = re.compile(r"([1-9]\d*)(?:x| x )([1-9]\d*)")
COORDINATE_REGEX = re.compile(r"([1-9]\d*)(?:,|, )([1-9]\d*)")


def ask_user_for_board_dimensions() -> tuple[int, int]:
    while True:
        board_dimensions = input(
            "Enter board dimensions ('size' or 'width x height'): "
        )

        if SQUARE_DIMENSIONS_REGEX.fullmatch(board_dimensions):
            board_size = int(board_dimensions)

            return board_size, board_size

        if match := RECTANGULAR_DIMENSIONS_REGEX.fullmatch(board_dimensions):
            return tuple(map(int, match.groups()))

        print("Invalid input. Try again")


def show_board(board: Board) -> None:
    for i, row in enumerate(board):
        if i > 0:
            print(f" {'─' * (len(board[0]) * 6 - 1)}")

        row_string = "|".join(f"{cell:^5}" for cell in row)

        print(f" {row_string}")


def ask_user_for_move(board: Board) -> tuple[int, int]:
    while True:
        coordinate = input(
            f"Enter the coordinate of the cell that you want to mark (row [1-{len(board)}], col [1-{len(board[0])}]): "
        )

        match = COORDINATE_REGEX.fullmatch(coordinate)

        if match is None:
            print("Invalid input. Try again")
            continue

        row, col = map(int, match.groups())

        if not (1 <= row <= len(board) and 1 <= col <= len(board[0])):
            print("The coordinate is outside the board")
            continue

        row -= 1
        col -= 1

        if board[row][col] != EMPTY_SYMBOL:
            print("That cell is already taken")
            continue

        return row, col
