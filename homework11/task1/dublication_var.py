"""
Vasya implemented nonoptimal Enum classes.
Remove duplications in variables declarations using metaclasses.
from enum import Enum
class ColorsEnum(Enum):
    RED = "RED"
    BLUE = "BLUE"
    ORANGE = "ORANGE"
    BLACK = "BLACK"
class SizesEnum(Enum):
    XL = "XL"
    L = "L"
    M = "M"
    S = "S"
    XS = "XS"
Should become:
class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")
class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")
assert ColorsEnum.RED == "RED"
assert SizesEnum.XL == "XL"
"""

class SimplifiedEnum(type):

    def __getattr__(self, key):
        # for x, y in vars(self).items():
        #
        #     if not x.endswith("__"):
        #         return x, y

        keys = [attr for attr in vars(self) if not callable(getattr(self, attr)) and not attr.endswith("__")]
        return self.__dict__.get()

class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")

print(ColorsEnum.RED)
# print(ColorsEnum.__dir__(ColorsEnum))
#
# class Example(object):
#     bool143 = True
#     bool2 = True
#     blah = False
#     foo = True
#     foobar2000 = False
#
# example = Example()
# members = [attr for attr in dir(example) if not callable(getattr(example, attr)) and not attr.endswith("__")]
# print (members)