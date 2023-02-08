# #1
#
# class UpperLetter:
#
#     def getString(self, text):
#         return text
#     def printString(self, text):
#         print(self.getString(text).upper())
#
# som = UpperLetter()
# som.printString(som.getString(input()))
#
# #2

class Square:
    def __init__(self, length):
        self.length = length



class Shape(Square):
    def __init__(self, length, width):
        super().__init__(length)

    def area(self, length):
        return self.length * 0

squa = Shape(int(input()), 0)
squa.area(squa)

#3

class Square:
    def __init__(self, length, width):
        self.length = length
        self.width = width


class Shape(Square):
    def __init__(self, length, width):
        super().__init__(length, width)

    def area(self, length, *width):
        print(self.length * self.width)

squa = Shape(int(input()), float(input()))
squa.area(squa)

#4

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def shift(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return (dx ** 2 + dy ** 2)

    def __str__(self):
        return f"Point({self.x}, {self.y})"


point1 = Point(10, 4)
point2 = Point(5, 12)

print(point1.distance(point2))
point1.shift(10, 1)

print(point1.distance(point2))
print(point2.__str__())
