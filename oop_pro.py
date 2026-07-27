from typing_extensions import override
from datetime import datetime

class Employee:
    def __init__(self, employee_number, name,salary):
        self.employee_number = employee_number
        self.name = name
        self.salary = salary

    def __str__(self):
        return f'Employee Number: {self.employee_number},    Name:  {self.name},    salary:  {self.salary},'

class Developer(Employee):
    def __init__(self,employee_number, name,salary, language:str,master_ai:bool):
        super().__init__(employee_number, name,salary)
        self.language = language
        self.master_ai = master_ai

    @override
    def annual_raise(self):
        self.salary *= 1.25

    def __str__(self):
        return f'{super().__str__()}     language:  {self.language},     {'master_ai'.title().replace('_',' ')}:  {self.master_ai}'



e = Employee(123,'My Employee',25_000)
print(e)

d = Developer(123,'My Developer',25_000,'english', True)
print(d)

