import time
import struct
import random
import hashlib

def slow_calculate(value):
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1,3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))

print(slow_calculate(range(501)))
answ = 0
for i in range(501):
    answ += sum(slow_calculate(range(501)))