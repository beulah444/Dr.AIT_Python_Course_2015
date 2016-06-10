__author__ = 'Dr.S.Gowrishankar'

#Write a program which repeatedly reads numbers until
# the user enters 'done'. Once 'done' is entered,
#print out the total, count, and average of the numbers.
#If the user enters anything other than a number,
#detect their mistake using try and except and print
#an error message and skip to the next number.

def AverageAndCountFinder():
    total = 0
    count = 0
    while True:
        num = raw_input("Enter a number: ")
        if num == 'done':
            print total, count, (total / count)
            break
        else:
            try:
                total += float(num)
            except:
                print "Invalid input"
                continue
        count += 1

AverageAndCountFinder()
