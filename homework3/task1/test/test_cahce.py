from task1.cache import cache


def test_cahce():
    time_num = 2

    @cache(time=time_num)
    def f(smth):
        return smth

    answer = f(23)

    assert all([f(23) is answer for i in range(time_num)]) is True


def test_cache_diff_param():
    @cache(3)
    def f(a):
        print('inside', a)
        return a

    assert f(1) == 1
    assert f(1) == 1
    assert f(2) == 2
    assert f(2) == 2
