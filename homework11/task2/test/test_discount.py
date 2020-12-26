import pytest
from task2.discount import Order


def morning_discount(order):
    return order * 0.5


def elder_discount(order):
    return order * 0.9


def test_order():
    assert Order(100, morning_discount).final_price() == 50
    assert Order(100, elder_discount).final_price() == 10
