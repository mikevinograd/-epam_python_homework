import os
from typing import Tuple

import pytest
from task3.maxmin import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        (os.path.join("data_files", "test1.txt"), (-1, 9)),
        (os.path.join("data_files", "test2.txt"), (-5, -1)),
        (os.path.join("data_files", "test3.txt"), (0, 0)),
        (os.path.join("data_files", "test4.txt"), (-2323, 9999)),
        (os.path.join("data_files", "test5.txt"), (0, 59)),
    ],
)
def test_min_max(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result
