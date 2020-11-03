import pytest
from task3 import check_fibonacci


@pytest.mark.parametrize(
    ["value", "expected_result"],
    [
        ((0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765), True),
        ((0, 0, 0, 0), False),
        ((0, 1, 1, 2, 3, 8), False),
        ((8, 13, 21), True),
        ((0, 1), False),
    ],
)
def test_check_fibonacci(value: int, expected_result: bool):
    actual_result = check_fibonacci(value)

    assert actual_result == expected_result
