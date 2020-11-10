"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def multiple_replace(target_str, replace_values=[":", ";", ",", ".", "(", ")", "?"]):
    for i in replace_values:
        target_str = target_str.replace(i, "")
    target_str = target_str.replace("  ", " ")
    return target_str


def text_filter(file_path: str, char_include: bool):
    with open(file_path, "r") as fi:
        text = []
        if char_include:
            text = fi.read().encode().decode("unicode-escape").splitlines()
        else:
            text = multiple_replace(
                fi.read().encode().decode("unicode-escape")
            ).splitlines()
        for numb, line in enumerate(text):
            text[numb] = line.split(" ")
        max_numb = [0 for x in range(10)]
        max_word = [0 for x in range(10)]
        for numb, line in enumerate(text):
            if len(line[-1]) >= 2 and line[-1][-1] == "-":
                text[numb + 1][0] = line.pop(-1)[:-1] + text[numb + 1][0][1:]
        return text


def get_longest_diverse_words(file_path: str) -> List[str]:
    text = text_filter(file_path, 0)
    max_numb = [0 for x in range(10)]
    max_word = [0 for x in range(10)]
    for line in text:
        for word in line:
            for top10_num, top10 in enumerate(max_numb):
                if word not in max_word and top10 < len(set(word)):
                    max_numb[top10_num] = len(set(word))
                    max_word[top10_num] = word
    return max_word


def get_rarest_char(file_path: str) -> str:
    text = text_filter(file_path, 1)
    dict = {}
    rar_symb_cnt = 0
    for line in text:
        for word in line:
            for char in word:
                if char in dict:
                    dict[char] += 1
                else:
                    dict[char] = 1
    for key in dict:
        if rar_symb_cnt < dict[key]:
            rar_symb_cnt = dict[key]
            rar_symb = key
    return key


def count_punctuation_chars(file_path: str) -> int:
    text = text_filter(file_path, 1)
    cnt = 0
    for line in text:
        for word in line:
            for char in word:
                if char in ("""!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""):
                    cnt += 1
    return cnt


def count_non_ascii_chars(file_path: str) -> int:
    ascii_string = """!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    text = text_filter(file_path, 1)
    cnt = 0
    for line in text:
        for word in line:
            for char in word:
                if char not in ascii_string:
                    cnt += 1
    return cnt


def get_most_common_non_ascii_char(file_path: str) -> str:
    ascii_string = """!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
    dict = {}
    comm_symb_cnt = 0
    text = text_filter(file_path, 1)
    for line in text:
        for word in line:
            for char in word:
                if char not in ascii_string:
                    if char in dict:
                        dict[char] += 1
                    else:
                        dict[char] = 1
    for key in dict:
        if comm_symb_cnt < dict[key]:
            comm_symb_cnt = dict[key]
            comm_symb = key
    return comm_symb
