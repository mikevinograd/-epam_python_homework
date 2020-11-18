import pytest


from task4.fizzbuzz import fizzbuzz


@pytest.mark.parametrize(
    ["num", "expected_result"],
    [
        (1, ["1"]),
        (5, ["1", "2", "Fizz", "4", "Buzz"]),
        (
            15,
            [
                "1",
                "2",
                "Fizz",
                "4",
                "Buzz",
                "Fizz",
                "7",
                "8",
                "Fizz",
                "Buzz",
                "11",
                "Fizz",
                "13",
                "14",
                "Fizz Buzz",
            ],
        ),
        (0, []),
        (-1, []),
    ],
)
def test_fizzbuzz(num, expected_result):
    actual_result = fizzbuzz(num)
    assert actual_result == expected_result
