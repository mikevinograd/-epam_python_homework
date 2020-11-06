"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.


def func(a, b):
    return (a ** b) ** 2


cache_func = cache(func)

some = 100, 200

val_1 = cache_func(*some)
val_2 = cache_func(*some)

assert val_1 is val_2

"""
from collections import Callable


def my_func(val, cache=dict()):
    if val not in cache:
        # compute val
        res = 2 * val
        print(f'{val} compute')
        cache[val] = res
    return cache[val]

my_func(100)
my_func(200)
my_func(100)


# def cache(func: Callable) -> Callable:
#     ...
