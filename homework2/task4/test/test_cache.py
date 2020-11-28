import pytest
import mock
from task4.cache import cached


def test_cache():
    mock_funk = mock.Mock()
    funk = mock_funk
    mock_funk = cached(mock_funk)
    mock_funk()
    mock_funk()
    mock_funk()
    assert funk.call_count == 1
