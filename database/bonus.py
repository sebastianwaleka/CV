import sqlite3


class DataBase():
    def __init__(self, db_name, *db_args):
        self.db_name = db_name  # Name of Data Base
        self.db_args = db_args  # Columns of just named Data Base
        try:
            conn = sqlite3.connect(f'{db_name}.sqlite')
        except:
            with open(f'{db_name}.sqlite', w) as db:
                db.read()
            conn = sqlite3.connect(f'{db_name}.sqlite')

        cur = conn.cursor()
        cur.execute(f'DROP TABLE IF EXISTS {db_name}')
        cur.execute(f'CREATE TABLE {db_name} {db_args}')
        conn.commit()
        conn.close()

    def add_to_database(self, *args):
        conn = sqlite3.connect(f'{self.db_name}.sqlite')
        cur = conn.cursor()
        cur.execute(f'INSERT INTO {self.db_name} {self.db_args} VALUES {args}')
        conn.commit()
        conn.close()

    # def select_branch(self):


db = DataBase('employees', 'name', 'last_name')

db.add_to_database('Sebastian', 'Waleka')
