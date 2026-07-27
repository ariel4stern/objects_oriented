from typing import override
from datetime import datetime


class MyCar:

    def __init__(self, type, model, color, engine_size, price, seats):
        # print(f'\nCreating {type}-{model}....')
        self.type = type
        self.model = model
        self.color = color
        self.engine_size = engine_size
        self.price = price
        self.seats = seats
        # print(f'{type}-{model}, Created Successfully !!\n')

    @override
    def __str__(self):
        return f'\n{datetime.now().strftime("%H:%M:%S")}-{self.type}\n{str(dict(self.__dict__))}\nCreated Successfully!'


subaru = MyCar('Subaru', 'B4 Top 2010', 'Light-Gold', 1994, '21,000', 5)
print(subaru)

toyota = MyCar('Supra', 'MK4', 'Light-Tourquise', 1662, '445,500', 3)
print(toyota)



class MyBank:

    def __init__(self, f_name, l_name, bank_name, balance):
        self.f_name = f_name
        self.l_name = l_name
        self.bank_name = bank_name
        self.balance = balance

    @override
    def __str__(self):
        return f'\n{datetime.now().strftime("%H:%M:%S")}-{self.f_name}-{self.l_name}\n{str(dict(self.__dict__))}\nManged Successfully!'

    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f'\nWithdraw {amount} left in balnce: {self.balance}')
        else:
            print(f'\nSorry {self.f_name} You R Too Broke to get {amount} ,Try Another Amount')

    def deposit(self, amount):
        self.balance += amount
        print(f'\nDeposit {amount} for {self.f_name}, Now balance = {self.balance}')


ariel_bank = MyBank('Ariel', 'Stern', 'Pepper', 30000)
print(ariel_bank)
ariel_bank.deposit(200)
ariel_bank.withdraw(200)
ariel_bank.withdraw(30000000)

# toyota = MyCar('Supra','MK4','Light-Tourquise', 1662,'445,500',3)
# print(toyota)

class Point:
    def __init__(self, x: float = 0, y: float = 0):
        self.x = x
        self.y = y

    def move_left(self, value: float = 0):
        self.x -= value

    def move_right(self, value: float = 0):
        self.x += value

    def move_up(self, value: float = 0):
        self.y -= value

    def move_down(self, value: float = 0):
        self.y += value

    def __str__(self):
        return f'Point (x={self.x:.2f} ,y={self.y:.2f})'


p1 = Point(x=5.4, y=8.1)
print(p1)
p1.move_right(2)
print(p1)
p1.move_left(5)
print(p1)
p1.move_up(3)
print(p1)
p1.move_down(8)
print(p1)


class Character:

    def __init__(self, name, power, game_time_minutes):
        self.name = name
        self.power = power
        self.game_time_minutes = game_time_minutes

    def __eq__(self, other):
        if isinstance(other, int | float):
            return self.power == other
        return self.power == other.power

    def __len__(self):
        return self.game_time_minutes

    def __str__(self):
        return f'name: {self.name}, power: {self.power}, game time minutes: {self.game_time_minutes}'


c1 = Character('Ariel', 4000, 110)
print(c1)

