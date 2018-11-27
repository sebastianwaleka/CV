import sqlite3


class DataBase():
    def __init__(self, db_name):
        self.db_name = db_name  # Name of Data Base
        try:
            with open(f'{db_name}.sqlite') as db:
                db.read()
            print(f'Data base named {db_name} already exists.')
            # conn = sqlite3.connect(f'{db_name}.sqlite')
        except:
            with open(f'{db_name}.sqlite', 'w') as db:
                db.read()
            print(f'Created data base named {db_name}.')
            # conn = sqlite3.connect(f'{db_name}.sqlite')


class Table():
    table_columns = ()
    def __init__(self, db_name, table_name):
        self.db_name = db_name
        self.table_name = table_name

    def create_table(self, *args):
        self.table_columns = self.table_columns + args
        conn = sqlite3.connect(f'{self.db_name}.sqlite')
        cur = conn.cursor()
        cur.execute(f'DROP TABLE IF EXISTS {self.table_name}')
        cur.execute(f'CREATE TABLE {self.table_name} {args}')
        conn.commit()
        conn.close()

    def add_to_table(self, *tab_args):
        if len(tab_args) == len(self.table_columns):
            conn = sqlite3.connect(f'{self.db_name}.sqlite')
            cur = conn.cursor()
            cur.execute(f'INSERT INTO {self.table_name} {self.table_columns} VALUES {tab_args}')
            conn.commit()
            conn.close()
        else:
            print('Number of arguments must be equal to number of columns in table')
            print(f'{len(tab_args)} - {len(self.table_columns)}')

    # def select_branch(self):


# db = DataBase('Warszawa')
tb = Table('Warszawa', 'Pracownicy')
# tb.create_table('ID','NAME','LAST_NAME','TARGET','SPRZEDAZ','REALIZACJA','KARTY','WKL')
tb.add_to_table(1,'Sebastian','Waleka',665000,100000,(100000/665000)*100,2,1000)
# tb.add_to_table(1,'Wojciech','Zielinski',500000,200000,(200000/500000)*100,1,500)