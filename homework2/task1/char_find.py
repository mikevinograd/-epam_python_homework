"""
Given a file containing text. Complete using only default collections:
    1) Find 10 longest words consisting from largest amount of unique symbols
    2) Find rarest symbol for document
    3) Count every punctuation char
    4) Count every non ascii char
    5) Find most common non ascii char for document
"""
from typing import List


def get_longest_diverse_words(file_path: str) -> List[str]:
    ...


def get_rarest_char(file_path: str) -> str:
    ...


def count_punctuation_chars(file_path: str) -> int:
    ...


def count_non_ascii_chars(file_path: str) -> int:
    ...


def get_most_common_non_ascii_char(file_path: str) -> str:
    ...


def multiple_replace(target_str, replace_values=[':', ';', ',', '.', '(', ')', '?']):
    # получаем заменяемое: подставляемое из словаря в цикле
    for i in replace_values:
        # меняем все target_str на подставляемое
        target_str = target_str.replace(i, '')
    target_str = target_str.replace('  ', ' ')
    return target_str


print(repr('\u00bbJetzt und hier\u00ab'))
with open('data.txt', 'r') as fi:
    # print(fi.readlines()[3])
    # print(set(fi.read()))
    text = []
    text = multiple_replace(fi.read()).splitlines()
    for numb, line in enumerate(text):
        text[numb] = line.split(' ')
    for numb, line in enumerate(text):
        if len(line[-1]) >= 2 and line[-1][-1] == '-':
            text[numb + 1][0] = line.pop(-1)[:-1] + text[numb + 1][0][1:]
        for word_numb,word in enumerate(line):
            # text[numb][word_numb] = repr(word)
            print(b"{}".format(word).decode("utf-8"))
    # for line in fi:
    #     text.append(fi.readline())
    # for i in text:
    #     print(i)
    # print(text, end='\n')
