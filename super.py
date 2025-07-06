#super() = Function used in a child class to call methods from a parent class (superclass)
#           It allows you to extend the fucntionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        #these are common to all the shapes
        self.color = color
        self.is_filled = is_filled  

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")      


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        #to use color and is_filled defined in parent class
        super().__init__(color, is_filled)
        self.radius = radius

    #as Circle also has describe method, this definition will be used whenever this method for circle is called
    #However, the fucntionality can be extended as well. See Square
    def describe(self):
        print(f"It is a circle with an area of {3.14*self.radius*self.radius}cm^2")
        

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width

    def describe(self):
        print(f"It is a sqaure with an area of {self.width**2}cm^2")
        #To extend the functionality i.e. to use the method definition in the parent class as well
        super().describe() 

        #In the above case the area line will be printed first and then the functionality defined in
        #the parent class. To reverse this super().describe() can be written above the print area line. See Triangle 

class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"It is a triangle with an area of {0.5*self.width*self.height}cm^2")



circle = Circle(color = "red", is_filled = True, radius = 5)
square = Square(color = "purple", is_filled = "True", width = 6)
triangle = Triangle(color = "white", is_filled = False, width = 10, height=6)

square.describe()
triangle.describe()