"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"
Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"
    [[-, -, o],
     [-, o, o],
     [x, x, x]]
     Return value should be "x wins!"
"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    def column_check(board):
        for i in range(3):
            if set(board[::][i]) == 1:
                return board[0][i]
            if "-" in board[::][i]:
                return "unfinished!!"

    def row_check(board):
        for i in range(3):
            if len(set(board[i][::])) == 1:
                return board[i][0]
            if "-" in board[i][::]:
                return "unfinished!!"

    def left_diagonal_check(board):
        left_diagonal = [board[i][i] for i in range(3)]
        if "-" in left_diagonal:
            return "unfinished!!"
        elif len(set(left_diagonal)) == 1:
            return left_diagonal[0]

    def right_diagonal_check(board):
        right_diagonal = [board[2 - i][i] for i in range(2, -1, -1)]
        if "-" in right_diagonal:
            return "unfinished!!"
        elif len(set(right_diagonal)) == 1:
            return right_diagonal[0]
    return row_check(board)
a =[["-", "-", "o"],
 ["-", "o", "o"],
 ["x", "x", "x"]]
print(tic_tac_toe_checker(a), a)
