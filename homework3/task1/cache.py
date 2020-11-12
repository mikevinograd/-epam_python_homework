def cache(time):
    def save(f):
        tmp = dict()
        tmp["time"] = time

        def wrap(*args, **kwargs):
            if tmp["time"] == time:
                result = f(*args, **kwargs)
                tmp["answ"] = result
            if tmp["time"] != 0:
                tmp["time"] -= 1
                print(tmp["answ"])
            else:
                tmp["time"] = time
            return tmp["answ"]

        return wrap

    return save
