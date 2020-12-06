import sqlite3
conn = sqlite3.connect('example.sqlite')
cursor = conn.cursor()
cursor.execute('SELECT * from presidents')
# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';") #[('presidents',), ('books',)]
# data = cursor.fetchall()   # will be a list with data.
# print(cursor.tables)
# print(data)
while row:=cursor.fetchone():
    print(row)

class TableData:
    