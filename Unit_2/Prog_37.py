__author__ = 'Dr.S.Gowrishankar'

#program to check whether a number is prime or not
num = int(raw_input('Enter a number'))

#prime numbers are greater than one
if num > 1:
    for i in range(2,num):
        if(num % i) == 0:
            print '{0} is not a prime number'.format(num)
            break
    if (num % i)is not 0:
        print '{0} is a prime number'.format(num)
else:
    print '{0} is not a prime number'.format(num)



