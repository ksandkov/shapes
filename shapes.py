import math
import random


class Shapes:
    def __init__(self, name: str):
        self.name = name


    def __str__(self):
        return "Name: " + self.name


#print(Shapes('NotSpam'))




class Circle(Shapes):
    def __init__(self, name, radius: int):
        super().__init__(name)
        self.radius = radius
    

    def get_area(self):
        area = self.radius * math.pi
        print("Area of Circle is:", end = ' ')
        return area


    def get_perimeter(self):
        perimeter = 2 * self.radius * math.pi
        print("Perimeter of Circle is:", end = ' ')
        return perimeter


shape = Circle("This is Circle", 25)
print(shape.name)
print(shape.get_area())
print(shape.get_perimeter())







class Rectangular(Shapes):
    def __init__(self):
       return "Name:{}; Shape1{}".format(
            self.name,
            self.shape
            )
    def get_area(self):
        pass

    def get_perimeter(self):
        pass







class Triangle(Shapes):
    def __init__(self):
       return "Name:{}; Shape1{}".format(
            self.name,
            self.shape
            )
    def get_area(self):
        pass

    def get_perimeter(self):
        pass

