import math


class Shapes:

    def __init__(self, name: str):
        self.name = name


    def __str__(self):
        return "Name: " + self.name


shape_0 = Shapes("This is Shapes Class")
print(shape_0) 
print( 50 * "=" )    


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


    def __str__(self):
        return 'Name: {} \n Radius: {}.'.format(
            self.name,
            self.radius,
        )
        
shape_1 = Circle("This is Circle", 25)
print(shape_1)
print(shape_1.get_area())
print(shape_1.get_perimeter())
print( 50 * "=" ) 


class Rectangle(Shapes):
    def __init__(self, name: str, a: int, b: int):
        super().__init__(name)
        self.a = a
        self.b = b

    def get_area(self):
        area = self.a * self.b
        print("Area of Rectangle is:", end=' ')
        return area


    def get_perimeter(self):
        perimeter = self.a + self.b
        print("Perimeter of Rectangle is:", end=' ')
        return perimeter


    def __str__(self):
        return 'Name: {} \n A: {}; \n B: {}.'.format(
            self.name,
            self.a,
            self.b,
        )

shape_2 = Rectangle("This is Rectangle", 2, 5)
print(shape_2)
print(shape_2.get_area())
print(shape_2.get_perimeter())
print( 50 * "=" ) 


class Triangle(Shapes):
    def __init__(self, name: str, a: int, b: int, c: int):
        super().__init__(name)
        self.a = a
        self.b = b
        self.c = c


    def get_area(self):
        p = (self.a + self.b + self.c) / 2
        area = math.sqrt(p * ((p - self.a) * (p - self.b) * (p - self.c)))
        print("Area of Triangle is:", end=' ')
        return area


    def get_perimeter(self):
        perimeter = self.a + self.b + self.c
        print("Perimeter of Triangle is:", end=' ')
        return perimeter


    def __str__(self):
        return 'Name: {} \n A: {}; \n B: {}; \n C: {}.'.format(
            self.name,
            self.a,
            self.b,
            self.c,
        )

shape_3 = Triangle("This is Triangle", 2, 3, 4)
print(shape_3)
print(shape_3.get_area())
print(shape_3.get_perimeter())
print( 50 * "=" ) 
