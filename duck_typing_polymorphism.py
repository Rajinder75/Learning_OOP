"""
Duck Typing = Another way to achive polymorphism besides Inheritance
                Objects must have the minimum necessary attributes/methods\
                "If it looks like a duck and quacks like a duck, it must be a duck."

"""

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("WOOF!")

class Cat(Animal):
    def speak(self):
        print("MEOW!")

class Car:

    alive = False #This can be set to False to override the True value of alive attribute in the parent class
    #def horn(self):
    #    print("HONK!") This will throw an error because of Car does not have a speak method
    def speak(self):
        print("HONK!")  #this will not because it has a speak function 


animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)