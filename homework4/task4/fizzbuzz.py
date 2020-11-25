"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.
That how first steps for the instruction may look like:
Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided
You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions
>>> fizzbuzz(5)
['1', '2', 'Fizz', '4', 'Buzz']
>>> fizzbuzz(0)
[]
>>> fizzbuzz(-5)
[]
>>> fizzbuzz(5.5)
Traceback (most recent call last):
        ...
TypeError: 'float' object cannot be interpreted as an integer
>>> fizzbuzz(15)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz']
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    fizz_buzz = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            fizz_buzz.append("Fizz Buzz")
        elif i % 3 == 0:
            fizz_buzz.append("Fizz")
        elif i % 5 == 0:
            fizz_buzz.append("Buzz")
        else:
            fizz_buzz.append(str(i))
    return fizz_buzz


if __name__ == "__main__":
    import doctest

    doctest.testmod()
