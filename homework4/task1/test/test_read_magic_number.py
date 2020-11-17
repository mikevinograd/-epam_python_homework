import os
import sys

import pytest

sys.path.append(os.path.abspath('..'))

from task1.read_magic_number import read_magic_number


@pytest.fixture()
def file_gen(file_pass, val):
    with open(file_pass, "w") as fi:
        fi.write(val)


@pytest.mark.parametrize(
    ["file_pass", "val"],
    [
        ('data0.txt', '1'),
        ('data1.txt', '2.5'),
        ('data2.txt', '2.99\n56\n24\n'),
        ('data3.txt', '1\n'),
    ],
)
def test_read_magic_number_true(file_pass, val, file_gen):
    # print(file_pass, val)
    actual_result = read_magic_number(file_pass)
    os.remove(file_pass)
    assert actual_result is True

@pytest.mark.parametrize(
    ["file_pass", "val"],
    [
        ('data0.txt', '-10'),
        ('data1.txt', '0'),
        ('data2.txt', '3\n56\n24\n'),
        ('data3.txt', '0.99\n'),
    ],
)
def test_read_magic_number_false(file_pass, val, file_gen):
    # print(file_pass, val)
    actual_result = read_magic_number(file_pass)
    os.remove(file_pass)
    assert actual_result is False

@pytest.mark.parametrize(
    ["file_pass", "val"],
    [
        ('data0.txt', 'sad'),
        ('data1.txt', 'qwd'),
        ('data2.txt', ''),
        ('data3.txt', '1error'),
    ],
)
def test_read_magic_number_value_error(file_pass, val, file_gen):
    with pytest.raises(ValueError):
        read_magic_number(file_pass)
    os.remove(file_pass)

