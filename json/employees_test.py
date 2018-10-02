'''
Tests for employees.
'''
import employee

def test_create_Employee():
    emp = employee.Employee('Jan', 'Kowalski', 5000, 1970)
    assert emp.name == 'Jan'
    assert emp.lastname == 'Kowalski'
    assert emp.salary == 5000
    assert emp.birth_year == 1970

def test_add_new_employee():
    emp = employee.Employee('Jan', 'Kowalski', 5000, 1970)
    assert emp.add_employee() == [{
        'name': 'Jan',
        'last_name': 'Kowalski',
        'salary': 5000,
        'birth_year': 1970
    }]
