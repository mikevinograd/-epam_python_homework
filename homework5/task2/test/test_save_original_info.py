import pytest
import functools
from task2.save_original_info import print_result, save_params


@print_result
def custom_sum(*args):
    """This function can sum any objects which have __add___"""
    return functools.reduce(lambda x, y: x + y, args)


def test_print_result():
    assert (
        custom_sum.__doc__
        == """This function can sum any objects which have __add___"""
    )
    assert custom_sum.__name__ == "custom_sum"


def test_print_result_stdout(capfd):
    custom_sum([1, 2, 3], [4, 5])
    stdout, stderr = capfd.readouterr()
    assert stdout == "[1, 2, 3, 4, 5]\n"
    assert stderr == ""


def test_print_result_nostdout(capfd):
    without_print = custom_sum.__original_func
    stdout, stderr = capfd.readouterr()
    assert without_print(1, 2, 3, 4) == 10
    assert stdout == ""
    assert stderr == ""
