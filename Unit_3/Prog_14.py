__author__ = 'Dr.S.Gowrishankar'

#Initialize init with some value and increment that value by passing
#another value using methods
#Do not use default values

class Increment_Exammple:
    def __init__(self, x):
        self.x = x

    def Actual_Increment_Here(self, y):
        return self.x + y


inc = Increment_Exammple(5)
print inc.Actual_Increment_Here(5)


