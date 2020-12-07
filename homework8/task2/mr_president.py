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
        self.cursor = sqlite3.connect(self.database_name).cursor()
        self.table = self.cursor.execute(f'SELECT * from {self.table_name}')

    def database_conn(self, func):
        def wrapper(*args, **kwargs):
            self.cursor = sqlite3.connect(self.database_name).cursor()
            # self.cursor.execute(f'SELECT * from {self.table_name}')  # where name = "Yeltsin"
            func_result = func(*args, **kwargs)
            self.cursor.close()
            return func_result

        return wrapper

    @database_conn
    def __len__(self):
        self.cursor.execute(f'SELECT * from {self.table_name}')
        len_ctn = 0
        row = self.cursor.fetchone()
        while row is not None:
            len_ctn += 1
            row = self.cursor.fetchone()
        # self.cursor.close()
        return len_ctn

    def __iter__(self):
        return self

    def __next__(self):
        row = self.table.fetchone()
        while row is not None:
            return row
        raise StopIteration

    def __getitem__(self, key):
        single_data_row = self.cursor.execute(f'SELECT * from {self.table_name} where name = "{key}"')
        return single_data_row.fetchone()

    def __contains__(self, value):
        return value in self.cursor.execute(f'SELECT * from {self.table_name} where name = "{value}"').fetchone()


examp = TableData(database_name='example.sqlite', table_name='presidents')

print(len(examp))
# print(examp['name'])
# print('Yeltsin' in examp)
# for president in examp:
#     print(list(president))
# for president in examp:
#     print(president)
# print(examp.table.fetchone(), examp.table.fetchone(), examp.table.fetchone())
