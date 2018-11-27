import bonus

def test_bonus_branch_create():
    db = bonus.DataBase('Oddzialy', 'Id','Nazwa', 'Target', 'Realizacja', 'Wykonanie', 'Pozostalo')
    assert db.db_name == 'Oddzialy'
    assert db.db_args == ('Id','Nazwa', 'Target', 'Realizacja', 'Wykonanie', 'Pozostalo')