class Shape():
    name = "name"
    color = "color"

    def describe(self):
        self.name = "name"
        self.color = "Green"


class Circle(Shape):
    radius = 3

    def c_area(self):
        self.area_calc = self.radius ** 2 * 3.14

    def print_c_area(self):
        self.c_area()
        print(f"circle area: {self.c_area}")
        print(f"color: {self.color}")


class Rectangle(Shape):
    def __init__(self):
        self.r_side = 3

    def r_area(self):
        self.r_area_calc = self.r_side ** 2

    def print_r_area(self):
        self.r_area()
        print(f"Rectangle area: {self.r_area}")
        print(f"color: {self.color}")


class Triangle(Shape):
    base = 3
    height = 5

    def t_area(self):
        self.t_area_calc = self.base * self.height

    def print_t_area(self):
        self.t_area()
        print(f"Triangle  area: {self.t_area}")
        print(f"color: {self.color}")
