"""
Write a function that takes directory path, a file extension and an optional tokenizer.
It will count lines in all files with that extension if there are no tokenizer.
If a the tokenizer is not none, it will count tokens.
For dir with two files from hw1.py:
# >>> universal_file_counter(test_dir, "txt")
6
# >>> universal_file_counter(test_dir, "txt", str.split)
6
"""
import os
from functools import partial
from pathlib import Path
from typing import Optional, Callable


def universal_file_counter(
        dir_path: Path, file_extension: str, tokenizer: Optional[Callable] = None
) -> int:
    if tokenizer is None:
        ctn_lines = 0
        for file in os.listdir(dir_path):
            if file.endswith(f".{file_extension}"):
                with open(f"{dir_path}/{file}") as f:
                    for i, _ in enumerate(f):
                        pass
                ctn_lines += i + 1
        return ctn_lines

    ctn_lines = 0
    for file in os.listdir(dir_path):
        if file.endswith(f".{file_extension}"):
            with open(f"{dir_path}/{file}") as f:
                for token in map(tokenizer, f):
                    ctn_lines += len(token) - 1
    return ctn_lines
