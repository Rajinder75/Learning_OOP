#object = A bundle of related attributes (variables) and methods (functions)
#       Example - phone, cup, book
#       You need a "class" to create manu objects

#class = (Blueprint) used to design the structure and layout of an object.


#the code for the class has been moved to a different file "car.py"
from car import Car

#          model   year    color    for_sale
car1 = Car("Mustang", 2024, "red", False)
car2 = Car("Corvette", 2025, "blue", True)
car3 = Car("Charger", 2026, "yellow", True)

"""It is a good practice to use the latter approach to access class variables
because this way it can be easily distinguished if they are class variables or instance variables"""
print(car1.wheels)
print(Car.wheels)