from circle import Circle
from square import Square

r = int(input("Enter the radius of the circle: "))

c = Circle(r)

a = c.get_area()
p = c.get_perimeter()

print(a)
print(p)

c.diameter = 200
print(c.get_perimeter())

s = Square(int (input("input square side")))

print(s.get_area())
print(s.get_perimeter())