import pytest
from typing import Any
from task1.tree import find_occurrences

example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        }
    },
    "fourth": "RED",
}


@pytest.mark.parametrize(
    ["tree", "element", "expected_result"], [
        (example_tree, "RED", 6),
        (example_tree, ["simple", "list", "of", "RED", "valued"], 1),
        (example_tree, "Some element that not in tree", 0)
    ]
)
def test_find_occurrences(tree: dict, element: Any, expected_result: int):
    actual_result = find_occurrences(tree, element)
    assert actual_result == expected_result
