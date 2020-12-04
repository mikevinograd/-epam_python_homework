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

    unfinished = False
    for i in range(3):
        print(board[::][i], board[i][::])
        if len(set([x[i] for x in board])) == 1 and "-" not in [x[i] for x in board]:
            return f"{board[0][i]} wins!"
        if len(set(board[i])) == 1 and "-" not in board[i]:
            return f"{board[i][0]} wins!"
        if "-" in board[::][i]:
            unfinished = True

    left_diagonal = [board[i][i] for i in range(3)]
    if len(set(left_diagonal)) == 1 and "-" not in left_diagonal:
        return f"{left_diagonal[0]} wins!"

    right_diagonal = [board[2 - i][i] for i in range(2, -1, -1)]
    if len(set(right_diagonal)) == 1 and "-" not in right_diagonal:
        return f"{right_diagonal[0]} wins!"

    if unfinished:
        return "unfinished!"
    return "draw!"

a =[["-", "o", "x"],
 ["-", "-", "x"],
 ["-", "o", "x"]]
print(tic_tac_toe_checker(a))
