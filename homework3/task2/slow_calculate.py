"""
Here's a not very efficient calculation function that calculates something important::
    import time
    import struct
    import random
    import hashlib
    def slow_calculate(value):
        #Some weird voodoo magic calculations
        time.sleep(random.randint(1,3))
        data = hashlib.md5(str(value).encode()).digest()
        return sum(struct.unpack('<' + 'B' * len(data), data))
Calculate total sum of slow_calculate() of all numbers starting from 0 to 500.
Calculation time should not take more than a minute. Use functional capabilities of multiprocessing module.
You are not allowed to modify slow_calculate function.
"""
import time
import struct
import random
import hashlib
from multiprocessing import Pool


def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def timeit(func):
    def timed(*args, **kw):
        ts = time.time()
        result = func(*args, **kw)
        te = time.time()
        print("Compilation time is: ", te - ts)
        return result

    return timed

@timeit
def call_func(arr, func):
    p = Pool(30)
    return sum(p.map(func, arr))


if __name__ == "__main__":
    call_func(list(range(0, 501)), slow_calculate)

