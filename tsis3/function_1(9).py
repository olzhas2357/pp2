
class Sheap:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Square:
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self, length, width):
        print(self.length * self.width)

squa = Shape(int(input()), 0)
squa.area(1, 3)
