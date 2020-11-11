from datetime import datetime


def printer(time):
    def save(f):
        d = {}
        d["time"] = time

        def wrap(*args, **kwargs):
            if d["time"] == time:
                result = f(*args, **kwargs)
                d["answ"] = result
            if d["time"] != 0:
                d["time"] -= 1
                print(d["answ"])
            else:
                d["time"] = time
            return d["answ"]

        return wrap

    return save


@printer(time=3)
def f():
    return input("? ")
