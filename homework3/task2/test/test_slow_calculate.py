from task2.slow_calculate import slow_calculate, call_func


def test_slow_calculate():
    assert 1025932 == call_func(list(range(0, 501)), slow_calculate)
