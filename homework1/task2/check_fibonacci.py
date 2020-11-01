"""
Given a cell with "it's a fib sequence" from slideshow,
    please write function "check_fib", which accepts a Sequence of integers, and
    returns if the given sequence is a Fibonacci sequence
We guarantee, that the given sequence contain >= 0 integers inside.

"""
from collections.abc import Sequence


def check_fibonacci(data: Sequence) -> bool:
    '''
    Check is given Sequence of int a Fibonacci Sequence
    :param data: Sequence of int
    :return: is it Fib Sequence
    '''
    if len(data) < 3 or data[1] == 0:
        return False

    # check if list < 3 and if it's full of zeros
    for i in range(2, len(data)):
        if data[i - 1] + data[i - 2] != data[i]:
            flag = False
            return False
    return True
