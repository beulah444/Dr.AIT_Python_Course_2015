m__author__ = 'Dr.S.Gowrishankar'

# create a class called Fridge and consider the following attributes eggs, milk, cheese.
# if the contents are greater than 2 for eggs, 3 for milk and 4 for cheese then display appropriate message.
# write separate method to check for each condition

class Fridge:
    def __init__(self, eggs, milk, cheese):
        self.eggs = eggs
        self.milk = milk
        self.cheese = cheese

    def checkEggs(self):
        if(self.eggs >= 2):
            print "Sufficient Quantity"
        else:
            print 'Insufficient Quantity'

    def checkMilk(self):
        if(self.milk >= 3):
            print "Sufficient Quantity"
        else:
            print 'Insufficient Quantity'

    def checkCheese(self):
        if(self.cheese >= 4):
            print "Sufficient Quantity"
        else:
            print 'Insufficient Quantity'


print 'First Case'
f = Fridge(2,3,4)
f.checkEggs()
f.checkCheese()
f.checkMilk()

print '****************'

print 'Second Case'
f = Fridge(2,2,3)
f.checkEggs()
f.checkCheese()
f.checkMilk()
