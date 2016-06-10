__author__ = 'Dr.S.Gowrishankar'

#write pythonic code to display the Fibinacci sequences up to nth term where n is provided by the user

nterms = int(raw_input('How many terms?'))

n1 = 0
n2 = 1
count = 2

#check if the number of terms are valid

if nterms <=0:
    print 'Please enter a positive number'
elif nterms == 1:
    print 'Fibonacci sequence'
    print '1'
else:
    print "Fibonacci sequence"
    print n1,n2,
    while count < nterms:
        nth = n1 + n2
        print nth,
        n1 = n2
        n2 = nth
        count += 1



