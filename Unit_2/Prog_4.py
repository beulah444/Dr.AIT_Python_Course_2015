__author__ = 'Dr.S.Gowrishankar'

#check whether a number is prime or not using while loop
#Input from user
num = int(raw_input("Enter a number: "))

#Variable declaration
i = 2

#while loop
while i <=(num - 1):
    if num % i == 0:
        print "Not a prime number"  #Display if not prime number
        break
    i += 1

#Display if prime number
if i == num:
    print "Prime number"
