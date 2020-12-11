import pytest
from task2.counter import instances_counter


def test_instances_counter():

    @instances_counter
    class User:
        pass

    zero_count = User.get_created_instances()
    user, _, _ = User(), User(), User()
    three_count = User.get_created_instances()
    _ = User()
    four_count = User.get_created_instances()
    assert zero_count == 0
    assert three_count == 3
    assert four_count == 4


def test_instances_reset():
    
    @instances_counter
    class User:
        pass

    user, _, _ = User(), User(), User()
    three_count = User.reset_instances_counter()
    zero_count = User.get_created_instances()
    assert three_count == 3
    assert zero_count == 0
