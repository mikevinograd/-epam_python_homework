"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""
import string

def custom_range(iterable_values, stop:str, start=None, step=1):
    # return iterable_values[start:stop:step]
    val_list = list(iterable_values)
    if start is None:
        return iterable_values[0:val_list.index(stop):step]
    else:
        start, stop = stop, start
        return iterable_values[val_list.index(start):val_list.index(stop):step]

print(custom_range(string.ascii_lowercase, 'g'))
print(custom_range(string.ascii_lowercase, "g"))
print(custom_range(string.ascii_lowercase, "g", "p"))
print(custom_range(string.ascii_lowercase, "p", "g", -2))
print(custom_range("pure", "r"))