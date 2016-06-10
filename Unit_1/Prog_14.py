__author__ = 'Dr.S.Gowrishankar'

# Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Input
# Enter Hours: 45
# Enter Rate: 10

# Output
# Pay: 475.0

inp = raw_input('Enter Hours: ')
hours = float(inp)
inp = raw_input('Enter Rate: ')
rate = float(inp)
if hours > 40:
    pay = hours * rate + (hours - 40) * rate * 0.5
else:
    pay = hours * rate
print 'Pay:', pay
