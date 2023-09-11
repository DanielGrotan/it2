from tic_tac_toe.cli import ask_user_for_board_dimensions, ask_user_for_move, show_board
from tic_tac_toe.constants import EMPTY_SYMBOL, PLAYER_SYMBOLS
from tic_tac_toe.game_logic import check_for_winner
from tic_tac_toe.types import Board


def game_loop(board: Board, consecutive_to_win: int) -> None:
    current_player_index = 0

    for _ in range(len(board) * len(board[0])):
        current_player_symbol = PLAYER_SYMBOLS[current_player_index]

        print(f"Player {current_player_symbol}'s turn")

        row, col = ask_user_for_move(board)
        board[row][col] = current_player_symbol

        show_board(board)

        if check_for_winner(board, current_player_symbol, row, col, consecutive_to_win):
            print(f"Player {current_player_symbol} won!")
            break

        current_player_index = (current_player_index + 1) % 2

    print("Draw")


def main() -> None:
    board_width, board_height = ask_user_for_board_dimensions()
    consecutive_to_win = min(board_width, board_height)

    board: Board = [
        [EMPTY_SYMBOL for _ in range(board_width)] for _ in range(board_height)
    ]

    show_board(board)
    game_loop(board, consecutive_to_win)


if __name__ == "__main__":
    main()
