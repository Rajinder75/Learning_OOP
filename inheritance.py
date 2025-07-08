#Inheritance = Allows a class to inherit attributes and methods from another class
#               Helps with code reusability and extensibility
#               Just like a child (subclass) inherits stuff from his parents (superclass)

#superclass
class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")
    
    def sleep(self):
        print(f"{self.name} is sleeping")

#the below classes (sub classes) will inherit from Animal class
class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

class Mouse(Animal):
    def speak(self):
        print("Squeek!")


dog = Dog("Scooby")
cat = Cat("Garfield")
mouse = Mouse("Mockey")

# print(mouse.name)
# print(mouse.is_alive)
# mouse.eat()
# dog.speak()

