"""
Given a list of integers numbers "nums".
You need to find a sub-array with length less equal to "k", with maximal sum.
The written function should return the sum of this sub-array.
Examples:
    nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3
    result = 16
"""
from typing import List
import copy


def find_maximal_subarray_sum(nums: List[int], k: int) -> int:
    if len(nums) < k or k == 0:
        return "Error! K should be <= amount of elements in array. K shouldn't be 0"
    max_sub = copy.copy(nums[:k])
    for i in range(k, len(nums) + 1):
        if sum(max_sub) < sum(nums[i - k : i]):
            max_sub = copy.copy(nums[i - k : i])
    return sum(max_sub)
