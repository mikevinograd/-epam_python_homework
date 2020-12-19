import pytest
from pathlib import Path
from task1.file_merge import merge_sorted_files


def test_file_merge(tmpdir):
    tmpdir.join(f"text1.txt").write("1\n3\n4\n5\n7\n")
    tmpdir.join(f"text2.txt").write("0\n2\n6\n")
    tmpdir.join(f"text3.txt").write("-1\n-2\n-3\n0\n")

    assert list(merge_sorted_files([f"{Path(str(tmpdir))}/text1.txt", f"{Path(str(tmpdir))}/text2.txt"])) == list(
        range(8))
