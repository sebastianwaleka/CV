import bonus

def test_bonus_DBcreate():
    db = bonus.DataBase('Oddzialy')
    assert db.db_name == 'Oddzialy'

def test_bonus_TableCreate():
    tb = bonus.Table('Oddzialy','Pracownicy','ID','NAME','LAST_NAME','TARGET','SPRZEDAZ')
    assert tb.db_name == 'Oddzialy'
    assert tb.table_name == 'Pracownicy'
    assert tb.tab_col == ('ID','NAME','LAST_NAME','TARGET','SPRZEDAZ')
