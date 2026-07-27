from abc import ABC
from typing_extensions import override
from datetime import datetime

# class Person(ABC):
#     def __init__(self,age:int):
#         self.age = age
#         #self.__age=age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self,value):
#         if value < 0:
#             raise ValueError('Age must be greater than 0')
#         else:
#             self.__age = value
#
#     @override
#     def __str__(self):
#         return f'age: {self.age}    '

# p = Person(-20)
# print(f'{p}\n')


#                                                                                Targil ----->  1
# Part 1 (20 min) — Base class + _init_ + _str_
# Create class Media
# Fields (private):
# __title (str) must be at least 2 character and
#                  not all space
# __year (int) must be >= 1888
#   *getter year return how long ago 2024 --> 2
# __minutes (int) must be > 0
#   *getter return i.e. 1 hour 3 minutes if > 60
# Tasks:
# _init_(title, year, minutes) with validation
# _str_ like: "Media(title='...', year=..., minutes=...)"
# Add getters for all fields
#   add reasonable conditions

class Media(ABC):
    def __init__(self,title:str,year:int,minutes:int):
        self.title = title
        self.year = year
        self.minutes = minutes

    @property
    def title(self):
        return f'------{self.__title}------'
    @title.setter
    def title(self,value):
        if not value or len(value.strip()) < 2:
            raise ValueError('Title must have at least 2 non-space characters!')
        else:
            self.__title = value

    @property
    def year(self):
        t_year = datetime.now().year
        return int(t_year) - self.__year

    @year.setter
    def year(self,value):
        t_year = datetime.now().year
        if not value or value < 1889:
            raise ValueError('Year must be greater than 1888!')
        elif value > 2026:
            raise ValueError(f'We are not in the future(today is {t_year})!')
        else:
            self.__year = value

    @property
    def minutes(self):
        if self.__minutes > 61:
            hours = self.__minutes //60
            mins = self.__minutes % 60
            return f"{hours} hour(s) and {mins} minute(s)"
        else:
            return f"{self.__minutes} minute(s)"

    @minutes.setter
    def minutes(self,value):
        if value < 0:
            raise ValueError('Minutes must be greater than 0')
        else:
            self.__minutes = value


    def __eq__(self,other): # title
        return self.__title.replace(' ', '').lower() == other.__title.replace(' ', '').lower()

    def __gt__(self,other): # minutes
        return self.__minutes > other.__minutes

    def __ge__(self,other): # minutes
        return self.__minutes >= other.__minutes

    def __lt__(self,other): # minutes
        return self.__minutes < other.__minutes

    def __le__(self,other): # minutes
        return self.__minutes <= other.__minutes

    @override
    def __str__(self):
        return f"title = '{self.__title.title()}'    ,year = {self.__year}      ,minutes = '{self.__minutes}'"

m = Media(title='title!!',year=2002,minutes=72)
print(f'{m}\n')
print(f'{m.title}\n')
print(f'{m.year}\n')
print(f'{m.minutes}\n')

class Movie(Media):
    def __init__(self,title:str,year:int,minutes:int,director:str,budget:float):
        super().__init__(title,year,minutes)
        self.director = director
        self.budget = budget

    @property
    def budget(self):
        return self.__budget
    @budget.setter
    def budget(self,value):
        if not value or value < 0:
            raise ValueError('Budget must have at least more then 0 Shekel!')
        else:
            self.__budget = value

    @property
    def director(self):
        return self.__director
    @director.setter
    def director(self,value):
        if not value or len(value.strip()) < 5:
            raise ValueError('Budget must be at least 5 characters!')
        else:
            self.__director = value

    @override
    def __str__(self):
        return f'Movie({super().__str__()}  ,Budget = {self.__budget}  ,Director = {self.__director})'

class Series(Media):
    def __init__(self,title:str,year:int,minutes:int,season:int,episodes:int):
        super().__init__(title,year, minutes)
        self.season = season
        self.episodes = episodes

    @property
    def season(self):
        return self.__season
    @season.setter
    def season(self,value):
        if not value or value < 1:
            raise ValueError('Season must be greater than 0!')
        else:
            self.__season = value

    @property
    def episodes(self):
        return self.__episodes
    @episodes.setter
    def episodes(self, value):
            if not value or value < 0:
                raise ValueError('Invalid Season value!')
            else:
                self.__episodes = value

    @override
    def __str__(self):
        return f'Series({super().__str__()}  ,Season = {self.__season}  ,Episodes = {self.__episodes})'

movie1 = Movie(title='Kong fu panda',year=2002,minutes=72,director='Ariel',budget=200000)
print(f'{movie1}\n')
#print(f'{movie1.title}\n')

movie2 = Movie(title='Kong  fu panda',year=2002,minutes=72,director='Ariel',budget=200000)
print(f'{movie2}\n')
#print(f'{movie2.title.strip()}\n')
print(f'{movie1 == movie2}\n')

series1 = Series('Breaking  bad',2002,135,200,15)
print(f'{series1}\n')

series2 = Series('Breaking  bad',2002,135,200,15)
print(f'{series2}\n')
print(f'{series1 == series2}\n')

#                                                                                Targil ----->  2
# Implement _eq_: compare title.lower() + year
#   if the same --> return true otherwise false

# Implement _gt_: compare minutes
#         _ge_ _lt_ le__  >= > < <=

# class Movie inherits Media
#   field __director getter setter check len(director) > 4
#   field __budget getter setter check > 0

# class Series inherites Media
#   field __season __episodes
#      season > 0 episodes > 0
#      season > episodes
# _str_


