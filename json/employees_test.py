'''
Tests for employees.
'''
from employee import *


def test_create_Employee():
    employee = Employee('Jan', 'Kowalski', 5000, 40)
    assert employee.name == 'Jan'
    assert employee.lastname == 'Kowalski'
    assert employee.salary == 5000
    assert employee.age == 40