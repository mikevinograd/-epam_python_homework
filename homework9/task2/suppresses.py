"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.
# >>> with supressor(IndexError):
...    [][2]
"""
from contextlib import contextmanager


class Supressor:
    def __init__(self, exeption):
        self.exeption = exeption

    def __enter__(self):
        pass

    def __exit__(self, type, value, traceback):
        try:
            yield
        except self.exeption:
            pass


@contextmanager
def supressor(exeption):
    try:
        try:
            yield
        finally:
            pass
    except exeption:
        pass
