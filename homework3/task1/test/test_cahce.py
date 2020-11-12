from task1.cache import cache


def test_cahce():
    time_num = 2

    @cache(time=time_num)
    def f(smth):
        return smth

    answ = f(23)

    assert all([f(23) is answ for i in range(time_num)]) is True
