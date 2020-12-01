import sqlite3


class MySQLite:
    def __init__(self, db_name):
        self.__db_name = db_name

    def __enter__(self):
        self.__db = sqlite3.connect(self.__db_name)
        self.__cur = self.__db.cursor()
        return self.__cur

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.__db.commit()
        self.__db.close()


create_tables = 'CREATE TABLE IF NOT EXISTS test_table(' \
                'col_1 INT NOT NULL,' \
                'col_2 TEXT NOT NULL)'

with MySQLite('test.db') as m:
    m.execute(create_tables)
    m.execute('INSERT INTO test_table (col_1, col_2) VALUES(1, "test")')
    m.execute('SELECT * FROM test_table')
    rows = m.fetchall()
    print(rows)
