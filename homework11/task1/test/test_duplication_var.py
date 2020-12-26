import pytest
from task1.dublication_var import SimplifiedEnum


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


def test_SimplifiedEnum():
    assert ColorsEnum.BLUE == "BLUE"
    assert ColorsEnum.BLACK == "BLACK"
    assert ColorsEnum.RED == "RED"


def test_SimplifiedEnum_error():
    with pytest.raises(ValueError):
        assert ColorsEnum.ERROR
