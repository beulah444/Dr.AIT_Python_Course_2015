try:
    length = float(raw_input('Enter the length of the rectangle'))
    breadth = float(raw_input('Enter the Breadth of the rectangle'))
    radius = float(raw_input('Enter a radius of circle'))
except:
    print 'Enter a number'
    exit(0)

area = length * breadth
perimeter = 2 * length + 2 * breadth

print area
print perimeter

circleArea = 3.14 ** radius
circumference = 2 * 3.14 * radius

print circleArea
print circumference
