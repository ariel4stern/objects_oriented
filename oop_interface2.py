from abc import ABC, abstractmethod
from typing_extensions import override

class Person(ABC):
    def __init__(self,id:int, name):
        self.id = id
        self.name = name

    @override
    def __str__(self):
        return f'ID: {self.id}    ,Name: {self.name}    '

class ArnonaPay(ABC):
    @abstractmethod
    def payArnona(self):
        pass

class RentPay(ABC):
    @abstractmethod
    def payRent(self):
        pass

class Tenant(Person,ArnonaPay,RentPay):
    def __init__(self,id_num:int,name,arnona:float, rent:float,address):
        super().__init__(id_num,name)
        self.arnona = arnona
        self.rent = rent
        self.address = address

    @override
    def payRent(self):
        return self.rent

    @override
    def payArnona(self):
        return self.arnona

    @override
    def __str__(self):
        return f'{super().__str__()}  ,Arnona: {self.arnona}    ,Rent: {self.rent}    ,Address: {self.address}'

p = Person(0,'Ariel')
print(f'{p}\n')

p2 = Tenant(2,'Ariel2',250,2500,'Elad')
print(p2)
print(f'{p2}    Arnona ===== {p2.payArnona()}\n')

p3 = Tenant(3,'Ariel3',356,4510,'Elad')
print(p3)
print(f'{p3}    Rent ===== {p3.payRent()}\n')

