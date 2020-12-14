"""
Write a function that merges integer from sorted files and returns an iterator
file1.txt:
1
3
5
file2.txt:
2
4
6
list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list) -> Iterator:
    with open(file_list[0]) as fi1:
        with open(file_list[1]) as fi2:
            tmp_file1 = fi1.readline().rstrip('\n')
            tmp_file2 = fi2.readline().rstrip('\n')
            while tmp_file1 != "" and tmp_file2 != "":
                if int(tmp_file1) < int(tmp_file2):
                    yield int(tmp_file1)
                    tmp_file1 = fi1.readline().rstrip('\n')
                else:
                    yield int(tmp_file2)
                    tmp_file2 = fi2.readline().rstrip('\n')

            while tmp_file1 == "":
                if tmp_file2 == "":
                    break
                yield int(tmp_file2)
                tmp_file2 = fi2.readline().rstrip('\n')

            while tmp_file2 == "":
                if tmp_file1 == "":
                    break
                yield int(tmp_file1)
                tmp_file1 = fi1.readline().rstrip('\n')
