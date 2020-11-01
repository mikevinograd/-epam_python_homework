import os
from typing import Tuple

import pytest
from task03.maxmin import find_maximum_and_minimum


@pytest.mark.parametrize(
    ["file_name", "expected_result"],
    [
        (os.path.join("data_files", "test1"), ()),
        (os.path.join("data_files", "test2"), ()),
        (os.path.join("data_files", "test3"), ()),
        (os.path.join("data_files", "test4"), ()),
        (os.path.join("data_files", "test5"), ()),
    ],
)
def test_min_max(file_name: str, expected_result: Tuple[int, int]):
    actual_result = find_maximum_and_minimum(file_name)

    assert actual_result == expected_result