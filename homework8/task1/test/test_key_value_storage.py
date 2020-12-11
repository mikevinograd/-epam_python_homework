import pytest
from task1.key_value_storage import KeyValueStorage


def test_key_val_store_brackets_check():
    actual_result = KeyValueStorage("task.txt")
    assert actual_result["name"] == "kek"
    assert actual_result["last_name"] == "top"


def test_key_val_store_dot_check():
    actual_result = KeyValueStorage("task.txt")
    assert actual_result.name == "kek"
    assert actual_result.last_name == "top"


def test_key_val_store_int_type_check():
    actual_result = KeyValueStorage("task.txt")
    assert type(actual_result.power) == int
    assert type(actual_result["power"]) == int


def test_key_val_store_value_check():
    actual_result = KeyValueStorage("task.txt")
    with pytest.raises(AttributeError, match="Invalid characters in attribute name"):
        actual_result["1"]
