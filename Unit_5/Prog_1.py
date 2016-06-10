__author__ = 'Dr.S.Gowrishankar'

import urllib

fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
   print line.strip()

