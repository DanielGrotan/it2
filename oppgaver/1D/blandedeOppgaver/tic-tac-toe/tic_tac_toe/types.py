from typing import Literal

PlayerSymbol = Literal["X", "O"]
EmptySymbol = Literal["□"]

Board = list[list[PlayerSymbol | EmptySymbol]]
