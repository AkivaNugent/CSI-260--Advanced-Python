from circle import Circle

r = int(input("Enter the radius of the circle: "))

c = Circle(r)

a = c.get_area()
p = c.get_perimeter()

print(a)
print(p)

c.diameter = 200

print(c.get_perimeter())