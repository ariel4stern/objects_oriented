from abc import ABC, abstractmethod
from typing_extensions import override

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

    @override
    def __str__(self):
        return f'Name: {self.name}'

class Flyable(ABC):
    @abstractmethod
    def fly(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    @override
    def move(self):
        print(f'{self.name.title()} is Running')

class Bat(Animal,Flyable):
    def __init__(self, name):
        super().__init__(name)

    @override
    def move(self):
        print(f'{self.name.title()} is Crawls')

    @override
    def fly(self):
        pass

class Eagle(Animal,Flyable):
    def __init__(self, name):
        super().__init__(name)

    @override
    def move(self):
        print(f'{self.name.title()} is Walks and Hops')

    @override
    def fly(self):
        pass

