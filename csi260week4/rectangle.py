class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width



    def get_area(self):
        return self.length * self.width


    def get_perimeter(self):
        return (self.length + self.width ) * 2