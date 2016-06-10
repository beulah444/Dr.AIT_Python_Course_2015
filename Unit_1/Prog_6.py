__author__ = 'Dr.S.Gowrishankar'

radius = 0.0
diameter = 0.0
circumference = 0.0
area = 0.0
Pi = 3.14159265

print "Input the diameter of the table:",
diameter = float(raw_input())
radius = diameter/2.0
circumference = 2.0*Pi*radius
area = Pi*radius*radius

print "\nThe circumference is ", circumference
# print "\nThe circumference is %f" %circumference
print "\nThe area is ", area