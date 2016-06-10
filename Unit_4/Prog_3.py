__author__ = 'Dr.S.Gowrishankar'

class PriorityQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def insert(self, item):
        self.items.append(item)

#At the beginning of each iteration,
#maxi holds the index of the biggest item (highest priority)
# we have seen so far. Each time through the loop,
#the program compares the i-eth item to the champion.
#If the new item is bigger, the value of maxi if set to i.
#When the for statement completes, maxi is the index of the biggest item.
#This item is removed from the list and returned.
    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]: maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi+1] = []
        return item

q = PriorityQueue()
q.insert(11)
q.insert(12)
q.insert(14)
q.insert(13)
while not q.is_empty():
    print q.remove()

