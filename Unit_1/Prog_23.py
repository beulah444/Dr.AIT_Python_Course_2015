__author__ = 'Dr.S.Gowrishankar'

#print the square of a numberm

# function definition
def square(x):
    y = x * x
    return y

#Input from user
#a = raw_input("Enter any number: ")
print "Enter any number: "
a = 4.5
print a

b = square(a) #function call

#Result
print "Square of %f is %f" %( a, b )
