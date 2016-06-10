__author__ = 'Dr.S.Gowrishankar'

#Write Pythonic code to read a web page using urllib and
#then use BeautifulSoup library to extract the href
#attributes from the anchor (a) tags.
import urllib
from BeautifulSoup import *

url = raw_input('Enter the URL')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)
# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print tag.get('href', None)
