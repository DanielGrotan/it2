def main() -> None:
    board = [[" "] * 3 for _ in range(3)]

    while True:
        row, col, symbol = input("Rad, kolonne, symbol: ").split(", ")

        row, col = int(row), int(col)

        if board[row][col] != " ":
            print("Ruten er allerede tatt")
            continue

        board[row][col] = symbol

        print(*board, sep="\n")

        for row in board:
            first_symbol = row[0]

            if first_symbol == " ":
                continue

            if all(symbol == first_symbol for symbol in row):
                print(f"{first_symbol} har tre på rad")
                return

        for col in range(3):
            first_symbol = board[0][col]

            if first_symbol == " ":
                continue

            if all(board[row][col] == first_symbol for row in range(0, 3)):
                print(f"{first_symbol} har tre på rad")
                return

        first_symbol = board[0][0]

        if first_symbol != " ":
            if board[1][1] == first_symbol and board[2][2] == first_symbol:
                print(f"{first_symbol} har tre på rad")
                return

        first_symbol = board[0][2]

        if first_symbol != " ":
            if board[1][1] == first_symbol and board[2][0]:
                print(f"{first_symbol} har tre på rad")
                return

        if all(all(symbol != " " for symbol in row) for row in board):
            print("Alle rutene er tatt uten at noen har tre på rad. Uavgjort!")


if __name__ == "__main__":
    main()
