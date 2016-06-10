__author__ = 'Dr.S.Gowrishankar'

astr = 'Bob'
try:
    print 'Hello'
    istr = int(astr)
    print 'There'  # This statement is not executed. Since there is an error in the previous statement.
except:
    istr = -1

print 'Done', istr

