"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
import unicodedata
import string


def tokenize(file_handler):
    buffer = ""
    char = " "
    while char:
        try:
            char = file_handler.read(1)
        except:
            continue
        if not char:
            break
        if unicodedata.category(char).startswith("P"):
            if buffer:
                yield ("word", buffer)
                buffer = ""
            yield ("punctuation", char)
            continue
        if char in string.whitespace:
            if buffer:
                yield ("word", buffer)
                buffer = ""
            yield ("whitespace", char)
            continue
        buffer += char
    if buffer:
        yield ("word", buffer)


def get_longest_deverse_words1(file_path):
    with open(file_path, "r", encoding="unicode-escape") as fi:
        top10_longest_words = ["" for x in range(10)]
        for token in list(tokenize(fi)):
            if token[0] == "word":
                for i, word in enumerate(top10_longest_words):
                    if token[1] not in top10_longest_words and len(set(token[1])) > len(
                        set(word)
                    ):
                        top10_longest_words[i] = token[1]
    return top10_longest_words


def char_tokenize(file_handler):
    char = " "
    while char:
        try:
            char = file_handler.read(1)
        except:
            continue
        if not char:
            break
        yield char


def get_rarest_char(file_path: str) -> str:
    with open(file_path, "r", encoding="unicode-escape") as fi:
        chars_dict = dict()
        for token in list(char_tokenize(fi)):
            if token in chars_dict:
                chars_dict[token] += 1
            else:
                chars_dict[token] = 1
    return sorted(chars_dict.items(), key=lambda item: item[1])[0][0]


def count_punctuation_chars(file_path: str) -> int:
    with open(file_path, "r", encoding="unicode-escape") as fi:
        chars_ctn = 0
        for token in list(char_tokenize(fi)):
            if unicodedata.category(token).startswith("P"):
                chars_ctn += 1
    return chars_ctn


def count_non_ascii_chars(file_path: str) -> int:
    with open(file_path, "r", encoding="unicode-escape") as fi:
        ascii_string = """!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        chars_ctn = 0
        for token in list(char_tokenize(fi)):
            if token not in ascii_string and token not in string.whitespace:
                print(token)
                chars_ctn += 1
    return chars_ctn


def get_most_common_non_ascii_char(file_path: str) -> str:
    with open(file_path, "r", encoding="unicode-escape") as fi:
        ascii_string = """!"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"""
        chars_dict = dict()
        for token in list(char_tokenize(fi)):
            if token not in ascii_string and token not in string.whitespace:
                if token in chars_dict:
                    chars_dict[token] += 1
                else:
                    chars_dict[token] = 1
    return sorted(chars_dict.items(), reverse=True, key=lambda item: item[1])[0][0]
