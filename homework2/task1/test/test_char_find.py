import pytest
import os
from task1.char_find import *


# task1 test1 get_longest_diverse_word
@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        (
            os.path.join("data.txt"),
            [
                "unmißverständliche",
                "Bevölkerungsabschub",
                "Kollektivschuldiger",
                "Selbstverständlich",
                "Werkstättenlandschaft",
                "Selbstbezichtigungen",
                "Vorausgeschickt",
                "Außerordentliche",
                "Machtbewußtsein",
                "Bilderabgleichung",
            ],
        ),
    ],
)
def test_get_longest_diverse_words(file, expected_result: list):
    actual_result = get_longest_deverse_words(file)
    assert actual_result == expected_result


# task1 test2 get_rarest_char
@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        (
            os.path.join("data.txt"),
            [
                "›",
                "‹",
                "0",
                "7",
                "8",
                "Y",
                "é",
                "Ä",
                "Ö",
                "'",
                ")",
                "î",
                "’",
                "X",
                "(",
                "›",
            ],
        ),
    ],
)
def test_get_rarest_char(file, expected_result: list):
    actual_result = get_rarest_char(file)
    assert actual_result in expected_result


# task1 test1 count_punctuation_chars
@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        (os.path.join("data.txt"), 5248),
    ],
)
def test_count_punctuation_chars(file, expected_result: list):
    actual_result = count_punctuation_chars(file)
    assert actual_result == expected_result


# task1 test1 count_non_ascii_chars
@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        (os.path.join("data.txt"), 2858),
    ],
)
def test_count_non_ascii_chars(file, expected_result: list):
    actual_result = count_non_ascii_chars(file)
    assert actual_result == expected_result


# task1 test1 get_most_common_non_ascii_char
@pytest.mark.parametrize(
    ["file", "expected_result"],
    [
        (os.path.join("data.txt"), "ä"),
    ],
)
def test_get_most_common_non_ascii_char(file, expected_result: list):
    actual_result = get_most_common_non_ascii_char(file)
    assert actual_result == expected_result
