from abc import abstractmethod, ABC
from typing import List


class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        ...


class Dog(Animal):

    def make_sound(self):
        return 'woof-woof'


class Cat(Animal):

    def make_sound(self):
        return 'meow'


class Chicken(Animal):

    def make_sound(self):
        return "cluck"


## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни


def animal_sound(animals: List[Animal]):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog(), Cat(), Chicken()]

animal_sound(animals)
