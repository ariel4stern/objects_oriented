from typing_extensions import override


class Vehicle:

    def __init__(self,name,base_fee:float):
        self.name=name
        self.base_fee=base_fee

    def trip_cost(self,distance_km:float):
        return self.base_fee + distance_km * 0

    def __str__(self):
        return f'Car Name:  {self.name},    Base Cost:  {self.trip_cost(0)}'

class GasCar(Vehicle):

    def __init__(self,liters_per_100km:float,price_per_liter:float,base_fee:float):
        super().__init__('GasCar',base_fee)
        self.liters_per_100km=liters_per_100km
        self.price_per_liter=price_per_liter

    @override
    def trip_cost(self,distance_km:float):
        fuel_used = (distance_km / 100) * self.liters_per_100km
        return self.base_fee + fuel_used * self.price_per_liter

    @override
    def __str__(self):
        return f'{super().__str__()},   Liter per 100km:    {self.liters_per_100km},    Price per liter:    {self.price_per_liter}'

class ElectricCar(Vehicle):

    def __init__(self,kwh_per_100km:float ,price_per_kwh:float ,base_fee:float):
        super().__init__('ElectricCar',base_fee)
        self.kwh_per_100km=kwh_per_100km
        self.price_per_kwh=price_per_kwh

    @override
    def trip_cost(self,distance_km:float):
        fuel_used = (distance_km / 100) * self.kwh_per_100km
        return self.base_fee + fuel_used * self.price_per_kwh

    @override
    def __str__(self):
        return f'{super().__str__()},   Kwh Per 100Km:  {self.kwh_per_100km},   Price Per Khm:  {self.price_per_kwh}'

class Taxi(Vehicle):
    def __init__(self,price_per_km:float ,is_night: bool ,base_fee:float):
        super().__init__('Taxi',base_fee)
        self.price_per_km=price_per_km
        self.is_night=is_night

    @override
    def trip_cost(self,distance_km:float):
        cost = self.base_fee + distance_km * self.price_per_km
        return (cost*1.20) if self.is_night else cost

    @override
    def __str__(self):
        return f'{super().__str__()},   Price per Km:  {self.price_per_km},    Night?   {self.is_night}'


v1 = Vehicle('Volkswagen',500)
print(v1,f'\n')

gc = GasCar(10,7,25)
gc_km = 100
print(gc)
print(f'{gc},   Trip cost(distance = {gc_km}): {gc.trip_cost(gc_km)}\n')

ec = ElectricCar(20,5,25)
ec_km = 100
print(ec)
print(f'{ec},   Trip cost(distance = {ec_km}): {ec.trip_cost(ec_km)}\n')

tx = Taxi(12,False,25)
tx_km = 100
print(tx)
print(f'{tx},   Trip cost(distance = {tx_km}): {tx.trip_cost(tx_km)}\n')


