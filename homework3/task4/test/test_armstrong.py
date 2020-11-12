import pytest
from task4.armstrong import is_armstrong


@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        (153, True),
        (10, False),
        (0, True),
        (548834, True),
    ],
)
def test_is_armstrong(file, expected_result: list):
    actual_result = is_armstrong(file)
    assert actual_result == expected_result