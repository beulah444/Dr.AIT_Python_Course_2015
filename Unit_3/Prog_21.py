#Why do you need regular expressions in Python? Consider a file “ait.txt”.
# Write a Python program to read the file and look for lines of the form
#X-DSPAM1-Confidence: 0.8475
#X-DSPAM2-Probability: 0.458
#Extract the number from each of the lines using a regular expression.
# Compute the average of the numbers and print out the average.
# Also use try/except to handle bad file names.

import re

try:
    fileHandler = open('test1.txt')
except:
    print "The file doesn't exist"
    exit()

numlist = list()
for line in fileHandler:
    line = line.rstrip()
    stuff = re.findall('^X.*: ([0-9.]+)', line)
    numlist.append(float(stuff[0]))

average = sum(numlist)/len(numlist)
print average
