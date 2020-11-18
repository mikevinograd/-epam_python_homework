import os
from unittest.mock import Mock, patch
import pytest


from task2.count_dots_on_i import count_dots_on_i


@patch("urllib.request.urlopen")
def test_count_dots_on_i(mock_request):
    with open(os.path.dirname(os.path.abspath(__file__)) + "\html_data.txt", "r") as fi:
        file = fi.read()
        mock_request.return_value = Mock(read=Mock(return_value=file))
        assert count_dots_on_i("https://examplewhith7019i.com/") == 7019


def test_count_dots_on_i_error():
    with pytest.raises(ValueError):
        count_dots_on_i("https://examplewhith7019i.com/")
