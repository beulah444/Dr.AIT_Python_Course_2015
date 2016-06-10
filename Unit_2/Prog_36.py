__author__ = 'Dr.S.Gowrishankar'
#Program to check whether a string is palindrome or not
my_str = raw_input("Enter a string to check for palindrome")

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print 'The Entered string is palindrome'
else:
    print 'The Entered String is not Palindrome'
