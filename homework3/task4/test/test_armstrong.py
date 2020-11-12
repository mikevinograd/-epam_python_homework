import pytest
from task4.armstrong import is_armstrong


@pytest.mark.parametrize(
    ["val", "expected_result"],
    [
        (153, True),
        (10, False),
        (0, True),
        (548834, True),
    ],
)
def test_is_armstrong(val, expected_result):
    actual_result = is_armstrong(val)
    assert actual_result == expected_result
