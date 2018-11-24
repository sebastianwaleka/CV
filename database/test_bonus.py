import bonus

def test_bonus_branch_create():
    war = bonus.Branch('Warszawa',2850000)
    assert war.branch_name == 'Warszawa'
    assert war.target == 2850000