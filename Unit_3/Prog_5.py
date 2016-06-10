__author__ = 'Dr.S.Gowrishankar'

class Point:
    def __init__(self, x= 0, y=0):
        self.x = x
        self.y = y

    def distance_from_origin(self):
        return((self.x ** 2) + (self.y ** 2)) ** 0.5

print 'First Case'
p = Point(3,4)
print p.x
print p.y
print p.distance_from_origin()

print 'Second Case'
q = Point(5,12)
print q.x
print q.y
print q.distance_from_origin()

print 'Third Case'
r = Point() #you are not passing any values
print r.x
print r.y
print r.distance_from_origin()

