import math

class Circle:
    def __init__(self, radius: int):
        self.radius = radius
        self.diameter = diameter = 2 * radius
        self.pi = math.pi


    def get_radius(self):
        return self.radius


    def get_area(self):
        return self.pi * self.radius * self.radius


    def get_perimeter(self):
        return self.radius * self.pi * 2