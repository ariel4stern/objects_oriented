from abc import ABC, abstractmethod
from typing_extensions import override

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

    @override
    def __str__(self):
        return f'Name: {self.name}'

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    @override
    def make_sound(self):
        return 'haw haw'


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    @override
    def make_sound(self):
        return 'miaw miaw'


rex = Dog('Rex')
print(rex,'---- Sound::',rex.make_sound())


caty = Cat('Caty')
print(caty,'---- Sound:',caty.make_sound())





