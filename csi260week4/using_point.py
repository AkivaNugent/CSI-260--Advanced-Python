from point import Point
p = Point
x = int(input("Was is the length of one side: "))
y = int(input("Was is the length of another side: "))

p1 = p(x, y)

print("The distance from the origin equals:",p1.calculate(p))
print("Given a",x,"and",y,"triangle, the length of the hypotenuse equals:",p1.calculate(p))


