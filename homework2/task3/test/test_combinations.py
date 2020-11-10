import pytest
from task3.combinations import combinations


@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        (([1, 2], [3, 4]), ([(1, 3), (1, 4), (2, 3), (2, 4)])),
        (
            ([1, 2], [3, 4], [5, 6]),
            [
                (1, 3, 5),
                (1, 3, 6),
                (1, 4, 5),
                (1, 4, 6),
                (2, 3, 5),
                (2, 3, 6),
                (2, 4, 5),
                (2, 4, 6),
            ],
        ),
        (([1, 2]), [(1,), (2,)]),
    ],
)
def test_combinations(file, expected_result: list):
    actual_result = combinations(file)
    assert actual_result == expected_result
