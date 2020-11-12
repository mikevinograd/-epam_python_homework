import pytest
from task1.cache import cache


@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        ([3, 2, 3], (3, 2)),
        ([2, 2, 1, 1, 1, 2, 2], (2, 1)),
        ([0], (0, 0)),
        ([-5, 2, 7, 8, -5, 4, 9999], (-5, 2)),
    ],
)
def test_cahce(file, expected_result: list):
    actual_result = cache(file)
    assert actual_result == expected_result