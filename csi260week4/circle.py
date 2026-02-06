import math

class Circle:
    def __init__(self, radius: int):
        self.radius = radius


    def get_radius(self):
        return self.radius


    def get_area(self):
        return math.pi * self.radius * self.radius


    def get_perimeter(self):
        return self.radius * math.pi * 2