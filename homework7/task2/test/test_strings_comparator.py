import pytest
from task2.strings_comparator import backspace_compare


def test_backspace_compare_one_backspace():
    assert backspace_compare("ab#c", "ad#c") is True


def test_backspace_compare_some_backspace():
    assert backspace_compare("a##c", "#a#c") is True


def test_backspace_compare_negative():
    assert backspace_compare("a#c", "b") is False
