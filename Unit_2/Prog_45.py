#Write a Python program to read the file
#and count and print the lines that start
#with the word “From”. Use string method.
#Prompt the user for the file name.
#Also use try/except to handle bad file names.

fname = raw_input(' Enter the file name: ')
try:
    fhand = open(fname)
except:
    print ' File cannot be opened: ', fname
    exit()
count = 0
for line in fhand:
    if line.startswith('From'):
        count = count + 1
        print line
print 'There were', count, 'subject lines in', fname