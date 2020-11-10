import pytest
from task4.cache import cached


def test_cache():
    some = 100, 200

    def test_func1(a, b):
        return a ** b ** 2

    cache_func1 = cached(test_func1)
    val_1 = cache_func1(*some)
    val_2 = cache_func1(*some)
    assert val_1 is val_2

    cache_func2 = cached(range)
    val_1 = cache_func2(*some)
    val_2 = cache_func2(*some)
    assert val_1 is val_2
