__author__ = 'Dr.S.Gowrishankar'

#define a class called Cart which contains data attributes apple and orange.
#if the content of apple is greater than 5 then return an appropriate message
#if the contents of orange is greater than 10 then return an appropriate message

class Cart:
    def __init__(self, apple, orange):
        self.apple = apple
        self.orange = orange

    def appleContentsCheck(self):
        if self.apple >= 5:
            return 'Sufficient Quantity'
        else:
            return 'Insufficient Quantity'

    def orangeContentsCheck(self):
        if self.orange >= 10:
            return 'Sufficient Quantity'
        else:
            return 'Insufficient Quantity'

#First Case
fruits = Cart(3,11)

returnAppleMessage = fruits.appleContentsCheck()
returnOrangeMessage = fruits.orangeContentsCheck()
print returnAppleMessage
print returnOrangeMessage