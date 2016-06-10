__author__ = 'Dr.S.Gowrishankar'

print "Enter radius of a circle: "
radius = 5
print radius

#Function definition
def areaperi ( r ):
    a = 3.14 * r * r
    p = 2 * 3.14 * r
    return a,p

area,perimeter = areaperi ( radius ) #function call


#Result
print  "Area = ", area
print  "Perimeter = ", perimeter
