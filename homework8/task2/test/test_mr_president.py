import pytest
import os
import sqlite3
from task2.mr_president import TableData


@pytest.fixture
def tmp_table():
    path_to_file = os.path.join(os.path.dirname(__file__), "temp_test_table.db")
    if os.path.exists(path_to_file):
        os.remove(path_to_file)

    temp_table = path_to_file
    con = sqlite3.connect(temp_table)
    cursor_table = con.cursor()
    cursor_table.execute("CREATE TABLE presidents(name text, id integer, country text)")
    cursor_table.execute("INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)", ("Yeltsin", 999, "Russia"))
    cursor_table.execute("INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)", ("Trump", 1337, "USA"))
    cursor_table.execute("INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)",
                         ('Big Man Tyrone', 101, 'Kekistan'))
    con.commit()
    con.close()
    yield temp_table

    if os.path.exists(temp_table):
        os.remove(temp_table)


def test_len_table(tmp_table):
    presidents = TableData(tmp_table, "presidents")
    assert len(presidents) == 3


def test_brackets(tmp_table):
    presidents = TableData(tmp_table, "presidents")
    assert presidents["Yeltsin"] == ("Yeltsin", 999, "Russia")
    assert presidents["Trump"] == ("Trump", 1337, "USA")
    assert presidents["Big Man Tyrone"] == ('Big Man Tyrone', 101, 'Kekistan')


def test_iteration(tmp_table):
    presidents = TableData(tmp_table, "presidents")
    name_presidents = ("Yeltsin", "Trump", "Big Man Tyrone")
    for president, name_presidents in zip(presidents, name_presidents):
        assert president['name'] == name_presidents


def test_contains(tmp_table):
    presidents = TableData(tmp_table, "presidents")
    assert "Yeltsin" in presidents
    assert "Trump" in presidents
    assert "Big Man Tyrone" in presidents


def test_if_table_changed(tmp_table):
    presidents = TableData(tmp_table, "presidents")
    assert len(presidents) == 3
    con = sqlite3.connect(tmp_table)
    cursor_table = con.cursor()
    cursor_table.execute("INSERT INTO presidents(name, id, country) VALUES(?, ?, ?)", ("Sychev", 23, "Korea"))
    con.commit()
    con.close()
    assert len(presidents) == 4
