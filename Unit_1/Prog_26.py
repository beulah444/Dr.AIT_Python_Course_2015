__author__ = 'Dr.S.Gowrishankar'

try:
    year = int(raw_input('Enter a year'))
except:
    print 'Enter Year numerically'
    exit(0)


if(year % 100 == 0):
    if(year % 400 == 0):
        print 'Leap Year'
    else:
        print 'Not a Leap Year'
else:
    if year % 4 == 0:
        print 'Leap Year'
    else:
        print 'Not a Leap Year'

