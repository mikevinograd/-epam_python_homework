"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.
That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal by pressing win + R on Windows
 - Print cd and the path to directory, where the file contains
 - Ex: cd C:\Users\User\Documents\GitHub\-epam_python_homework\homework4\task4
 - Print python file_name -v
 - Ex: python fizzbuzz.py -v
 - Check tests!
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
>>> fizzbuzz(31)
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'Fizz Buzz', '16', '17', 'Fizz', '19', 'Buzz', 'Fizz', '22', '23', 'Fizz', 'Buzz', '26', 'Fizz', '28', '29', 'Fizz Buzz', '31']
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    Fizz_Buzz = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            Fizz_Buzz.append("Fizz Buzz")
        elif i % 3 == 0:
            Fizz_Buzz.append("Fizz")
        elif i % 5 == 0:
            Fizz_Buzz.append("Buzz")
        else:
            Fizz_Buzz.append(str(i))
    return Fizz_Buzz




if __name__ == "__main__":
    import doctest

    doctest.testmod()


