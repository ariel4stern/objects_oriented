import math

class Calculator:

    @staticmethod
    def add(a,b):
        print(a+b)

    @staticmethod
    def sub(a,b):
        print(a-b)

    @staticmethod
    def multiply(a,b):
        print(a*b)

    @staticmethod
    def divide(a,b):
        print(a/b)

    @staticmethod
    def power(a,d):
        print(a**d)

    @staticmethod
    def square(a):
        print(a**2)

    @staticmethod
    def square_root(a):
        print(math.sqrt(a))

class ValidEmail:
    @staticmethod
    def is_valid_email(email):
        print('@' in email)

    @staticmethod
    def is_strong_password(password):
        print(len(password) > 8)

#ValidEmail.is_valid_email('arielstern      1')
#ValidEmail.is_strong_password('8')

class Robot:
    population = 0

    def __init__(self, name):
        self.name = name
        Robot.population += 1

    def introduce(self):
        print(f'Hey Im {self.name}')

    @classmethod
    def reach_10(cls):
        return cls.population >= 10

    @staticmethod
    def valid_name(name):
        return len(name) > 1 and name.isalpha(name)

#print(Robot.population)

stu_names = ['Ariel','Nadav','Noam','Meir','Shlomi','Matan','Roi','Pinhas','Or','shalom']
for i in range(len(stu_names)):
    robot = Robot(stu_names[i].title())
    #robot.introduce()
    #print(Robot.population)
    #print(robot.reach_10())

class WeatherReport:
    fahr_minus_number = 32
    fahr_fraction = 5/9

    to_fahr_mul = 1.8
    to_fahr_add = 32

    def __init__(self, celsius):
        self.celsius = celsius

    # return true if temp above 40 or below 0
    @staticmethod
    def is_extreme(temp):
        return 40 < temp or temp < 0


    def display(self):
        return f"Celsius = {self.celsius}, Fahrenheit = {WeatherReport.from_celcius_to_fahrenheit(self.celsius)}"

    # convert F to C
    # Formula: (F - 32) * 5/9
    @classmethod
    def from_fahrenheit_to_celcius(cls,f_value):
        return (f_value-cls.fahr_minus_number) *cls.fahr_fraction


    # (°C × 1.8) + 32
    @classmethod
    def from_celcius_to_fahrenheit(cls,c_value):
        return (c_value*cls.to_fahr_mul) + cls.to_fahr_add


#print(WeatherReport.from_fahrenheit_to_celcius(40))
#w1 = WeatherReport(1)
#print(w1.display())
#w2 = WeatherReport(2)
#print(w2.display())