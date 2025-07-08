# multiple inheritance = inherit from more than one parent class
#                        C(A,B) - C inherits from both A and B

# multilevel inheritance = inherit froma parent which inherits from another parent
#                        C(B) <- B(A) <- A

class Animal():

    #because the constructor is in the Grandparent class, the name will be given to the children classes
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")

class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")

class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

#below are children classes
#The below classes will also have the eat and sleep abilities because Prey and Predator classes have
#inherited properties from the Animal Class
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

#fish are also prey and predators, so they will inherit from both the classes (multiple inheritance)
class Fish(Prey, Predator):
    pass


rabbit = Rabbit("Bugs")
hawk = Hawk('Tony')
fish = Fish("Nemo")

hawk.hunt()
rabbit.eat()