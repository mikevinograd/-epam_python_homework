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
from typing import Any, Sequence, Callable
import functools


def my_func(val):
    return val


my_func(100)
my_func(200)
my_func(100)


def cache(func: Callable) -> Callable:  # memoized
    # use memoization technique
    memoization_func = func

    def wrapper(*args):
        return memoization_func(args)

    return memoization_func

    # cache_dict = {}
    #
    # # @functools.wraps(func)
    # def inner(*args):
    #     # key = args, tuple(sorted(kwargs.items()))
    #     if args in cache_dict:
    #         return cache_dict[args]
    #     else:
    #         bi = cache_dict[args] = func(*args, **kwargs)
    #         return bi
    # return inner


a = cache(my_func(100))
b = cache(my_func(200))
c = cache(my_func(100))
print(id(a), id(c))
print(a is b)
