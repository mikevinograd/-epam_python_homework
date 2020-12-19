"""
We have a file that works as key-value storage, each like is represented as
 key and value separated by = symbol, example:
name=kek last_name=top song_name=shadilay power=9001
Values can be strings or integer numbers. If a value can be treated both as
 a number and a string, it is treated as number.
Write a wrapper class for this key value storage that works like this:
storage = KeyValueStorage('path_to_file.txt') that has its keys and values accessible as collection items and as
attributes. Example: storage['name'] # will be string 'kek'
storage.song_name # will be 'shadilay' storage.power # will be integer 9001
In case of attribute clash existing built-in attributes take precedence.
 In case when value cannot be assigned to an attribute (for example when there's a line 1=something) ValueError
 should be raised. File size is expected to be small, you are permitted to read it entirely into memory.
"""
import re


class KeyValueStorage:

    def __init__(self, path: str):
        self.path = path
        self.__filedata = self.reader()

    def reader(self):
        with open(self.path, "r") as fi:
            file_data = {}
            for line in fi.readlines():
                key, value = line.strip().split("=")
                if key not in file_data:
                    file_data[key] = int(value) if value.isdigit() else value
        return file_data

    def __getattr__(self, key):
        return self.__filedata[key]

    def __getitem__(self, key):
        if not re.match(r"^\w[\w\d\-]+$", key):
            raise AttributeError("Invalid characters in attribute name")
        return self.__filedata[key]
