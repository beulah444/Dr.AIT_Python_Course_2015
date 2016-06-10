__author__ = 'Dr.S.Gowrishankar'


# Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program.
# The following shows two executions of the program:

# Input
# Enter Hours: 20
# Enter Rate: nine

# output
# Error, please enter numeric input

# Input
# Enter Hours: forty

# Output
# Error, please enter numeric input

try:
   inp = raw_input('Enter Hours: ')
   hours = float(inp)
   inp = raw_input('Enter Rate: ')
   rate = float(inp)
   if hours > 40:
       pay = hours * rate + (hours - 40) * rate * 0.5
   else:
       pay = hours * rate
   print 'Pay:', pay
except:
   print 'Error, please enter numeric input'
