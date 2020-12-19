"""
Write a wrapper class TableData for database table, that when initialized with database name and table acts as
collection object (implements Collection protocol). Assume all data has unique values in 'name' column.
 So, if presidents = TableData(database_name='example.sqlite', table_name='presidents')
then
len(presidents) will give current amount of rows in presidents table in database
presidents['Yeltsin'] should return single data row for president with name Yeltsin
'Yeltsin' in presidents should return if president with same name exists in table
object implements iteration protocol. i.e. you could use it in for loops::
for president in presidents:
print(president['name'])
all above mentioned calls should reflect most recent data. If data in table changed after you created
 collection instance, your calls should return updated data.
Avoid reading entire table into memory. When iterating through records, start reading the first record,
then go to the next one, until records are exhausted. When writing tests, it's not always neccessary to mock database
calls completely. Use supplied example.sqlite file as database fixture file.
"""
import sqlite3


class TableData:
    def __init__(self, database_name: str, table_name: str):
        self.database_name = database_name
        self.table_name = table_name

    def database_conn(func):
        def wrapper(self, *args, **kwargs):
            conn = sqlite3.connect(self.database_name)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            result = func(self, cursor, *args, **kwargs)
            cursor.close()
            conn.close()
            return result

        return wrapper

    @database_conn
    def __len__(self, cursor):
        cursor.execute(f'SELECT COUNT(*) from {self.table_name}')
        row = cursor.fetchone()[0]
        return row

    @database_conn
    def __getitem__(self, cursor, key):
        single_data_row = cursor.execute(f'SELECT * from {self.table_name} where name =?', (key,))
        return tuple(single_data_row.fetchone())

    @database_conn
    def __contains__(self, cursor, value):
        return value in cursor.execute(f'SELECT * from {self.table_name} where name = "{value}"').fetchone()

    @database_conn
    def __iter__(self, cursor):
        conn = sqlite3.connect(self.database_name)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute(f'SELECT * from {self.table_name}')
        while True:
            row = cursor.fetchone()
            if row is not None:
                yield row
            else:
                break
