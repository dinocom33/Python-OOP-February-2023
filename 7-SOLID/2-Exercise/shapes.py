import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def get_area(self):
        ...


class Rectangle(Shape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, site, height):
        self.site = site
        self.height = height

    def get_area(self):
        return self.site * self.height / 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class AreaCalculator:

    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def shapes(self):
        return self.__shapes

    @shapes.setter
    def shapes(self, value):
        if not isinstance(value, list):
            raise ValueError("`shapes` should be of type `list`.")

        self.__shapes = value

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.get_area()

        return total


shapes = [Rectangle(1, 6), Triangle(2, 3), Square(4, 5), Circle(7)]
calculator = AreaCalculator(shapes)

print(f"The total area is: {calculator.total_area:.2f}")
