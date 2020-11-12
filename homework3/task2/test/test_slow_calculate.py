import time
from task2.slow_calculate import slow_calculate, call_func


def test_slow_calculate():
    if __name__ == "__main__":
        ts = time.time()
        result = call_func(list(range(0, 501)), slow_calculate)
        te = time.time()
        assert 1025932 == result
        assert te - ts < 60
