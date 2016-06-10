__author__ = 'Dr.S.Gowrishankar'

#count the occurrence of each of the word in the file and print the top 10 words and their occurence

fhand = open('mbox.txt')
counts = dict()

for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    lst.append((val, key))
lst.sort(reverse=True)

for val, key in lst[:10]:
    print key, val

