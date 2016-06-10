__author__ = 'Dr.S.Gowrishankar'

largest = None
print 'Before: ', largest

for itervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or itervar > largest:
        largest = itervar

print ' Largest: ', largest
