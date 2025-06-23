class Car:
        
    #class variables = Shared among all instances(objects) of a class
    #                    --defined outside the constructor 
    wheels = 4

    #constructor (it is a dunder method, i.e. it is written with double underscores)
    #self is already provided, the other parameters are the attributes 
    def __init__(self, model, year, color, for_sale ):
        #below are the instance variables
        # when the model, year etc are received they can be assigned to the object
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    #creating methods
    def drive(self):
                                #self refers to the current car(object) we are working with
        print(f"You drive the {self.color} {self.model}")

    def stop(self):
        print(f"You stop the {self.color} {self.model}")

    def describe(self):
        print(f"{self.year} {self.color} {self.model}")