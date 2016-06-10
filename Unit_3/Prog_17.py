import copy

def front_and_back(front):
    back = copy.copy(front)
    back.reverse()
    print str(front) + str(back)

myList = [1, 2, 3, 4]
front_and_back(myList)

