from collections import defaultdict


def cache(time):
    def save(f):
        tmp = defaultdict(dict)
        tmp["time"] = time

        def wrap(*args, **kwargs):
            result = tuple(args)
            if result in tmp and tmp[result][1] != 0:
                tmp[result][1] -= 1
            if result not in tmp or (result in tmp and tmp[result][1] == 0):
                tmp[result] = [f(*args, **kwargs), time]
            return tmp[result][0]

        return wrap

    return save
