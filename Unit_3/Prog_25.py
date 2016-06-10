#Write Pythonic code to demonstrate tuples by sorting
# a list of words from longest to shortest using loops.

txt = ' but soft what light in yonder window breaks '
words = txt.split()
t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)
res = list()
for length, word in t:
    res.append(word)

print res