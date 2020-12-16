import os
import pytest
from task2.suppresses import Supressor, supressor


def test_func_supressor():
    with supressor(IndexError):
        assert [][2]


def test_class_supressor():
    with Supressor(IndexError):
        assert [][2]
