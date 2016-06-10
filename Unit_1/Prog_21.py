__author__ = 'Dr.S.Gowrishankar'

#Function within Function

# function definitions
def argentina():
    print  "I am in argentina"

def brazil():
    print "I am in brazil"
    argentina() #function call

def italy():
    print "I am in italy"
    brazil() #function call
    print "I am back in italy"

print  "I am in main"
#function call
italy()

print "I am finally back in main"
