import pytest
import string
from task5.custom_range import custom_range

@pytest.mark.parametrize(
    ["iterable_values", "values", "expected_range"],
    [
        (string.ascii_lowercase, ["g"], ["a", "b", "c", "d", "e", "f"]),
        (
            string.ascii_lowercase,
            ["g", "p"],
            ["g", "h", "i", "j", "k", "l", "m", "n", "o"],
        ),
        (string.ascii_lowercase, ["g", "p", -2], ["p", "n", "l", "j", "h"]),
        ("makaroni", ["r", "i"], ['r', 'o', 'n']),
    ],
)
def test_custom_range(iterable_values, values, expected_range):
    actual_result = custom_range(iterable_values, *values)
    assert actual_result == expected_range