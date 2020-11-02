import pytest
from task5.max_subarray import find_maximal_subarray_sum


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (((0, 0, 0, 0), 2), 0),
        (
            ((0, 0, 0, 0), 5),
            "Error! K should be <= amount of elements in array. K shouldn't be 0",
        ),
        (
            ((0, 0, 0, 0), 0),
            "Error! K should be <= amount of elements in array. K shouldn't be 0",
        ),
        (((1, 2, 0, 3, 4, 8, 0, 4, 7, 9, 9, 1, 2, 3), 3), 25),
        (((1, 3, -1, -3, 5, 3, 6, 7), 3), 16),
        (((1, 3, -1, -3, 5, 3, 6, 7), 1), 7),
    ],
)
def find_maximal_subarray_sum(value: int, expected_result: bool):
    actual_result = find_maximal_subarray_sum(value)

    assert actual_result == expected_result
