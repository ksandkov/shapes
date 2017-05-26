class Shape:
    def __init__(self, name:str, age:str):
        pass




    def __str__(self):
        return "Name:{}; Shape{}".format(
            self.name,
            self.age
            )

    def __repr__(self):
        return "Name:{}; Shape{}".format(
            self.name,
            self.age
            )


class Circle(Shape):
    def __init__(self):
        pass