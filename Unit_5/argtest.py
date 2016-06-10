__author__ = 'Dr.S.Gowrishankar'

import sys

print 'Count', len(sys.argv)
print 'Type', type(sys.argv)

for arg in sys.argv:
   print 'Argument', arg


