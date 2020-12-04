"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.
Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any
from collections import defaultdict


def find_occurrences(tree: dict, element: Any) -> int:
    answer = defaultdict(int)

    def finder(struct, element):
        if struct == element:
            answer["ctn"] += 1
        if isinstance(struct, dict):
            for val in struct.values():
                finder(val, element)
        elif isinstance(struct, (list, tuple, set)):
            for elem in struct:
                finder(elem, element)

    finder(tree, element)
    return answer["ctn"]
