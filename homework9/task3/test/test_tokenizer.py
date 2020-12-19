import pytest
from functools import partial
from pathlib import Path
from task3.tokenizer import universal_file_counter


def test_universal_file_counter(tmpdir):
    tmpdir.join(f"text1.txt").write("0\n1\n2\n3\n4\n5\n6\n")
    tmpdir.join(f"text2.txt").write("7\n8\n9\n")
    tmpdir.join(f"text3.txt").write("-1\n-2\n-3\n")
    assert universal_file_counter(Path(str(tmpdir)), "txt") == 13


def test_universal_file_counter_split(tmpdir):
    tmpdir.join(f"text1.txt").write("0\n1\n2\n3\n4\n5\n6\n")
    tmpdir.join(f"text2.txt").write("7\n8\n9\n")
    tmpdir.join(f"text3.txt").write("-1\n-2\n-3\n")
    assert universal_file_counter(Path(str(tmpdir)), "txt", partial(str.split, sep="-")) == 3
