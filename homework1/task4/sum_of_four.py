"""
Classic task, a kind of walnut for you
Given four lists A, B, C, D of integer values,
    compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.
We guarantee, that all A, B, C, D have same length of N where 0 ≤ N ≤ 1000.
"""
from typing import List
from collections import defaultdict


def check_sum_of_four(a: List[int], b: List[int], c: List[int], d: List[int]) -> int:
    dict1 = defaultdict(int)
    dict2 = defaultdict(int)
    for i in range(len(a)):
        for j in range(len(a)):
            dict1[a[i] + b[j]] += 1
            dict2[c[i] + d[j]] += 1
    amount_zeroes = 0
    for key in dict1:
        if -key in dict2:
            amount_zeroes += dict1[key] * dict2[-key]
    return amount_zeroes
