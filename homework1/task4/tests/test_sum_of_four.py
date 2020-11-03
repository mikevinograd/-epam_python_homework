import pytest
from task4 import sum_of_four


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        (((5, 5, 5, 5, 0), (5, 5, 5, 5, 0), (1, 1, 1, 1, 1), (-1, 0, 0, 0, 0)), 5),
        (((0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0), (0, 0, 0, 0, 0)), 625),
        (((1, 1, 1, 1, 1), (1, 1, 1, 1, 1), (1, 1, 1, 1, 1), (1, 1, 1, 1, 1)), 0),
        (
            (
                (1, 2, 3, 4, 5),
                (25, 0, 1, 0, 0),
                (0, -1, 0, 0, -25),
                (-5, -4, -3, -2, -1),
            ),
            79,
        ),
    ],
)
def check_sum_of_four(value: int, expected_result: bool):
    actual_result = check_sum_of_four(value)

    assert actual_result == expected_result
