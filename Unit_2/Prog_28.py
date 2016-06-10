__author__ = 'Dr.S.Gowrishankar'

#count the occurence of each of the word in a file

count = dict()
fhand = open('mbox-short.txt')

for lines in fhand:
    words = lines.rstrip().split()

    for word in words:
        count[word] = count.get(word, 0) + 1

print count


