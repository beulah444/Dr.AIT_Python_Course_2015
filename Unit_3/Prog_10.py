__author__ = 'Dr.S.Gowrishankar'

class ListSum:
    def __init__(self, listArg):
        self.listArg = listArg

    def __init__(self, listArg):
                self.listArg = listArg

    def ComputeSum(self):
        print sum(self.listArg)

#a =[1,2,3,4,5]
#ls = ListSum(a) #no need to write these two lines
ls = ListSum([1,2,3,4,5]) # you can directly pass the list values
ls.ComputeSum()


