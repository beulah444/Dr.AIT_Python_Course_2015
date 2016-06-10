__author__ = 'Dr.S.Gowrishankar'

print "This program calculates the average of any number of values."
total = 0
count = 0
while True: # infinite loop
    print "\nEnter a value: ",
    value = float(raw_input())
    total += value
    count += 1

    print "Do you want to enter another value? (Y or N): ",
    answer = raw_input()
    if(answer == 'n'):
        break

print "The average is %.2f" %(total/count)
