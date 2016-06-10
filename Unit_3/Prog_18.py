import copy

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    def reverse(self):
        (self.x , self.y) = (self.y, self.x)

def front_and_back(front):
    back = copy.copy(front)
    back.reverse()
    print str(front) + str(back)

p = Point(3, 4)
front_and_back(p)


