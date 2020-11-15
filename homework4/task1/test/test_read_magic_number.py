import pytest
import os
from task1.read_magic_number import read_magic_number


@pytest.mark.parametrize(
    ["file_pass", "val"],
    [
        ('data0.txt', 1),
        ('data1.txt', 2.5),
        ('dat2.txt', '2.99\n56\n24\n'),
        ('data3.txt', '1\n'),
    ],
)
@pytest.fixture
def file_gen(file_pass, val):
    print('!!!')
    # with tempfile.TemporaryFile(mode= 'w+') as f:
    with open( file_pass, "w") as fi:
    # with open(os.path.join(os.pardir, file_pass), "w") as fi:
        file = fi.write(val)
        yield file
        # os.remove(file_pass)


def test_read_magic_number(file_pass, val, file_gen):
    file_gen
    actual_result = read_magic_number(file_pass)
    assert actual_result is True
# open(os.path.join(os.pardir, 'task1\data1.txt'), "w")
test_read_magic_number('data1.txt', 2.5)