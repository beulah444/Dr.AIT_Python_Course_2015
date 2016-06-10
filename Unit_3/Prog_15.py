__author__ = 'Dr.S.Gowrishankar'

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

p1 = Point(3, 4)
p2 = Point(5, 7)

p3 = p1 + p2
print p3

p4 = p1 * p2
print p4

p5 = p1 - p2
print p5
