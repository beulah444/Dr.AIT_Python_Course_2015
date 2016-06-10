__author__ = 'Dr.S.Gowrishankar'

# reverses the digits in a number

num = int(raw_input('Enter a number'))
rev = 0
rem = 0
while (num != 0):
    rem = num % 10
    rev = rev * 10 + rem
    num = num /10

print 'The reversed digits in a number is {0}'.format(rev)

