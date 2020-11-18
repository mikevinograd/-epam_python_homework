import pytest

from task3.my_precious_logger import my_precious_logger


def test_my_precious_logger_out(capfd):
    my_precious_logger("test")
    stdout, stderr = capfd.readouterr()
    assert stdout == "test"
    assert stderr == ""


def test_my_precious_logger_err(capfd):
    my_precious_logger("error: file not found")
    stdout, stderr = capfd.readouterr()
    assert stdout == ""
    assert stderr == "error: file not found"
