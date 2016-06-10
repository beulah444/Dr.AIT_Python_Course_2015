__author__ = 'Dr.S.Gowrishankar'

word = str(raw_input('Want to see if it is a palindrome?\n'))

def is_palindrome(word):
    if len(word) <= 2 and word[0] == word[-1]:
        print 'True'
    elif word[0] == word[-1]:
        is_palindrome(word[1:-1])
    else:
        print 'False'

is_palindrome(word)
