__author__ = 'Dr.S.Gowrishankar'

#finds the sum of digits in a number
num = int(raw_input('Enter a number'))
result = 0
rem = 0

while(num != 0):
    rem = num % 10
    result = result + rem
    num = num /10

print 'The sum of all digits is {}'.format(result)

