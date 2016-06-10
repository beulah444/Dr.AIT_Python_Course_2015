__author__ = 'Dr.S.Gowrishankar'

class Sum_Of_Elements:
    #you should always specify the __init__ even when you are not initializing
    #with any values
    def __init__(self):
        pass

    def sum_all_the_elements(self, list_Param):
        return sum(list_Param)

ls = Sum_Of_Elements() #creates an object

#you should declare an variable to hold the value that is returned from the method
sum_Of_All_Elements = ls.sum_all_the_elements([1,2,3,4,5])
print sum_Of_All_Elements

#Another way of combining the above two lines to print the output
#print ls.sum_all_the_elements([1,2,3,4,5])


