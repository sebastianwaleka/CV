import sqlite3

class DataBase():
    def __init__(self, db_name, *args):
        self.db_name = db_name
        self.args = args
        try:
            conn = sqlite3.connect(f'{db_name}.sqlite')
        except:
            with open(f'{db_name}.sqlite', w) as db:
                db.read()
            conn = sqlite3.connect(f'{db_name}.sqlite')

        cur = conn.cursor()
        cur.execute(f'DROP TABLE IF EXISTS {db_name}')
        cur.execute(f'CREATE TABLE {db_name} {args}')
        conn.commit()
        conn.close()

class Branch():
    def __init__(self, branch_name, target, sale = 0):
        self.branch_name = branch_name
        self.target = target
        self.sale = sale

    def add_to_database(self):
        conn = sqlite3.connect('branches.sqlite')
        cur = conn.cursor()
        cur.execute('DROP TABLE IF EXISTS branches')
        cur.execute('CREATE TABLE branches (num INT, branch TEXT, target FLOAT, sale FLOAT)')
        cur.execute('INSERT INTO branches (num, branch, target, sale) VALUES (?, ?, ?, ?)',
                    ('NULL', self.branch_name, self.target, self.sale))
        conn.commit()
        conn.close()

    # def select_branch(self):

db = DataBase('employees', 'name','last_name')

war = Branch('Warszawa',2850000)
war.add_to_database()
