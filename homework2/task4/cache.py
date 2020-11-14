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
from collections import defaultdict


def cached(f):
    cache = defaultdict(dict)
    cache_list = []

    def wrapped(*args, **kwargs):
        result = tuple(args)
        if result not in cache:
            cache[result] = f(*result)
        return cache[result]

    return wrapped


# def cached(f):
#     cache = defaultdict(dict)
#
#     def wrapped(*args, **kwargs):
#         tmp_a = args[0]
#         tmp_b = args[1]
#         if tmp_a not in cache or tmp_b not in cache[tmp_a]:
#             print(tmp_a, tmp_b)
#             result = f(*args, **kwargs)
#             cache[tmp_a][tmp_b] = result
#         return cache[tmp_a][tmp_b]
#
#     return wrapped
# import mock для тестов 58 minute
@cached
def test_cache(a, b):
    print(111)
    return a, b

    def test_func1(a, b):
        return a + b


a = dict()
val1 = test_cache(100, 200)
val2 = test_cache(100, 200)
val3 = test_cache(200, 100)
val5 = test_cache(200, 100)
val4 = test_cache(300, 400)

print(val1, val2, val3, val4)
