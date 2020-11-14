"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List, Tuple


def major_and_minor_elem(inp: List) -> Tuple[int, int]:
    cnt_elements = {}
    for i in inp:
        if i in cnt_elements:
            cnt_elements[i] += 1
        else:
            cnt_elements[i] = 1
    sort_cnt_elements = sorted(cnt_elements.items(), key=lambda item: item[1])
    return (sort_cnt_elements[-1][0], sort_cnt_elements[0][0])
