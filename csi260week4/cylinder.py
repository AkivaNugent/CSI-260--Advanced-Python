import math

class Cylinder:
    def __init__(self, radius: int, height: int):
        self.radius = radius
        self.height = height

    def get_base(self):
        return math.pi * self.radius * self.radius

    def get_s_area(self):
        return math.pi * 2 * self.radius * (self.radius + (2 * self.height))

    def get_perimeter(self):
        return (math.pi * 2 * self.radius) + (2 * self.height)

