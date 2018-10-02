'''
This program will add and display employees written in json file.
'''
import json


class Employee:
    def __init__(self, name, lastname, salary, birth_year):
        self.name = name
        self.lastname = lastname
        self.salary = salary
        self.birth_year = birth_year

    def add_employee(self):
        try:
            with open('employee.json') as f:
                self.employees = json.load(f)
        except FileNotFoundError:
            self.employees = []

        employee = {
            'name': self.name,
            'last_name': self.lastname,
            'salary': self.salary,
            'birth_year': self.birth_year
        }

        self.employees.append(employee)
        with open('employee.json', 'w') as f:
            json.dump(self.employees, f)

        return self.employees

    def print_employees(self):
        with open('employee.json') as f:
            data = json.load(f)
        for num, emp in enumerate(data):
            print(f'[{num}] - {emp["name"]} {emp["lastname"]} '
                  f'- SALARY: {emp["salary"]} - BIRTH YEAR: {emp["birth_year"]};')
