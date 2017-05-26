import math


class Shapes:
    def __init__(self, name: str):
        self.name = name


    def __str__(self):
        return "Name: " + self.name
    
    
class Circle(Shapes):
    def __init__(self, name, radius: int):
        super().__init__(name)
        self.radius = radius


    def get_area(self):
        area = self.radius * math.pi
        print("Area of Circle is:", end=' ')
        return area


    def get_perimeter(self):
        perimeter = 2 * self.radius * math.pi
        print("Perimeter of Circle is:", end=' ')
        return perimeter


shape_1 = Circle("This is Circle", 25)
print(shape_1.name)
print(shape_1.get_area())
print(shape_1.get_perimeter())