import math

class Point:
    def __init__(self, x: int, y: int): #coordinates
        self.x = x
        self.y = y

        self.move(x,y)

    def move(self, x: int, y: int):
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: 'Point'):
        return math.hypot(self.x - 0, self.y - 0)

p = Point #Instantiation
x = 6
y = 8
p1 = p(x, y)

print("The distance from the origin equals:",p1.calculate(p))
