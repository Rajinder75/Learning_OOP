"""
Polymorphism = Greek word that means to have many forms or faces
                Poly = Many
                Morphe = format

Two ways to achieve Polymorphism
        1. Inheritance = An object could be treated of the same type as a parent class
        2. "Duck Typing" = Object must have necessary attributes/methods
"""
from abc import ABC, abstractmethod

class Shape():

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side**2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5*self.base*self.height

class Pizza(Circle):
    def __init__(self, topping, radius):
        super().__init__(radius)  #to pass the radius
        self.topping = topping
        self.radius = radius


shapes = [Circle(4), Square(5), Triangle(6,7), Pizza("pepperoni", 15)]
#Each of the classes in the list have 2 forms For example - Circle() is a Circle and a Shape
#Also, Pizza is also a Circle and hence a shape

for shape in shapes:
    print(shape.area())


