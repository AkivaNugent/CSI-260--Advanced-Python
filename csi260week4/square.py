class Square:
    def __init__(self, side: int):
        self.side = side



    def get_area(self):
        return self.side * self.side


    def get_perimeter(self):
        return self.side * 4