__author__ = 'Dr.S.Gowrishankar'

class Point:
    def __init__(self, x= 0, y=0):
        self.x = x
        self.y = y

    def print_point(self, p): #takes an object as parameter
        print '(%s,%s)' % (str(p.x), str(p.y))

print 'First Case'
p = Point(3,4)

p.print_point(p) #We are passing the object itself as argument



