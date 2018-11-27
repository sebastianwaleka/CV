import sqlite3


class DataBase():
    def __init__(self, db_name):
        self.db_name = db_name  # Name of Data Base
        try:
            with open(f'{db_name}.sqlite') as db:
                db.read()
            print(f'Data base named {db_name} already exists.')
        except:
            with open(f'{db_name}.sqlite', 'w') as db:
                db.read()
            print(f'Created data base named {db_name}.')


class Table():

    def __init__(self, db_name, table_name, *tab_col):
        self.db_name = db_name
        self.table_name = table_name
        self.tab_col = tab_col

    def create_table(self):
        conn = sqlite3.connect(f'{self.db_name}.sqlite')
        cur = conn.cursor()
        cur.execute(f'DROP TABLE IF EXISTS {self.table_name}')
        cur.execute(f'CREATE TABLE {self.table_name} {self.tab_col}')
        conn.commit()
        conn.close()

    def add_to_table(self, *tab_args):
        conn = sqlite3.connect(f'{self.db_name}.sqlite')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO {self.table_name} {self.tab_col[1:]} VALUES {tab_args}')
        conn.commit()
        conn.close()


    def select_all(self):
        conn = sqlite3.connect(f'{self.db_name}.sqlite')
        cur = conn.cursor()
        cur.execute(f'SELECT * FROM {self.table_name}')
        for row in cur:
            print(row)
        conn.commit()
        conn.close()

    def select(self, *args):
        arguments = ''
        for arg in args:
            arguments = arguments + arg + ','
        conn = sqlite3.connect(f'{self.db_name}.sqlite')
        cur = conn.cursor()
        cur.execute(f'SELECT {arguments[:-1]} FROM {self.table_name}')
        for row in cur:
            print(row)
        conn.commit()
        conn.close()
