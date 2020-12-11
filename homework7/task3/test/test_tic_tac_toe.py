import pytest
from task3.tic_tac_toe import tic_tac_toe_checker


def test_tic_tac_toe_checker_row_win():
    field = [["o", "o", "x"],
             ["-", "-", "o"],
             ["x", "x", "x"]]
    assert tic_tac_toe_checker(field) == "x wins!"


def test_tic_tac_toe_checker_colm_win():
    field = [["x", "x", "o"],
             ["-", "-", "o"],
             ["x", "x", "o"]]
    assert tic_tac_toe_checker(field) == "o wins!"


def test_tic_tac_toe_unfinished():
    field = [["o", "o", "-"],
             ["-", "-", "o"],
             ["x", "-", "x"]]
    assert tic_tac_toe_checker(field) == "unfinished!"


def test_tic_tac_toe_unfinished():
    field = [["o", "o", "x"],
             ["x", "x", "o"],
             ["o", "x", "x"]]
    assert tic_tac_toe_checker(field) == "draw!"
