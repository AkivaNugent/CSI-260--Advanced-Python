from cylinder import Cylinder

def CalcCylinder():
    """Take dimensional inputs and calculate are and perimeter"""
    cyl = Cylinder(int(input("Enter radius: ")),
                   int(input("Enter Height: "))
                   )

    print(f' The area is:      {cyl.get_s_area():.2f}')
    print(f' The perimeter is: {cyl.get_perimeter():.2f}')


CalcCylinder()