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
    ["file_pass", "val", "ground_truth"],
    [
        ('data0.txt', '1', True),
        ('data1.txt', '2.5', True),
        ('data2.txt', '2.99\n56\n24\n', True),
        ('data3.txt', '1\n', True),
    ],
)
def test_read_magic_number(file_pass, val, ground_truth, file_gen):
    # print(file_pass, val)
    actual_result = read_magic_number(file_pass)
    os.remove(file_pass)
    assert actual_result is ground_truth

# open(os.path.join(os.pardir, 'task1\data1.txt'), "w")
# test_read_magic_number('data1.txt', 2.5)
# open( '../testfile.txt', "w")
