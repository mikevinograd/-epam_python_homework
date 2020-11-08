"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.

You may assume that that every list contain at least one element

Example:

assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import List, Any
import itertools


def combinations(*args: List[Any]) -> List[List]:
    res_list = [[]]
    for i, list_instance in enumerate(args):
        # print(i, list_instance)
        res_list = [x + [y] for x in res_list for y in list_instance]
        # print('res_list ', res_list)
    return res_list

def copy_combinations(*args: List[Any]) -> List[List]:
    res_list = []
    for i in args[0]:
        for j in args[1:]:
            for numb in j:
                print(i, numb)
                # res_list = res_list.append([i, numb])
    # for i, list_instance in enumerate(args):
    #     print(i, list_instance)
    #     res_list = [x + [y] for x in res_list for y in list_instance]
    #     print('res_list ', res_list)
    return res_list

a = [1, 2]
b = [3, 4]
c = [5, 6]
print(combinations(a, b, c))
print(copy_combinations(a, b, c))