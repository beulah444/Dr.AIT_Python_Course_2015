__author__ = 'Dr.S.Gowrishankar'

#Program to find the factorial of a number provided by the user

num = int(raw_input('Enter a number'))
factorial = 1

if num < 0:
    print "factorial doesn't exist for negative numbers"
elif num == 0:
    print 'The factorial of 0 is 1'
else:
    for i in range(1,num + 1):
        factorial = factorial * i

print 'The factorial of number is {0}'.format(factorial)



