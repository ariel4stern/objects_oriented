from abc import ABC, abstractmethod
from typing_extensions import override

class Chargeable(ABC):
    @abstractmethod
    def charge(self):
        pass
class Drivable(ABC):
    @abstractmethod
    def drive(self):
        pass


class Vehicle(ABC):
    def __init__(self,model:str):
        self.model = model

    @override
    def move(self):
        pass

    @override
    def __str__(self):
        return f'Model: {self.model}'

class ElectricCar(Vehicle,Chargeable,Drivable):

    def __init__(self,battery_level:float):
        super().__init__('ElectricCar')
        self.battery_level = battery_level

    @override
    def move(self):
        return 'The car move...'

    @override
    def drive(self):
        return 'Driving...'

    @override
    def charge(self):
        return f'Charging...{self.battery_level}'

    @override
    def __str__(self):
        return f'{super().__str__()}    ,Battery level: {self.battery_level}'

class ElectricScooter(Vehicle,Chargeable):

    def __init__(self,max_speed:float):
        super().__init__('ElectricScooter')
        self.max_speed = max_speed

    @override
    def move(self):
        return 'Moving...'

    @override
    def charge(self):
        return 'Charging...'

    @override
    def __str__(self):
        return f'{super().__str__()}    ,Max speed: {self.max_speed}'


v1 = Vehicle('Mk4')
print(v1)

v2 = ElectricCar(88.2)
print(v2)
print(v2.move())
print(v2.drive())
print(v2.charge())

v3 = ElectricScooter(422)
print(v3)
print(v3.move())
print(v3.charge())

