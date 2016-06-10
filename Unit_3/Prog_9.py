__author__ = 'Dr.S.Gowrishankar'

#create a class called Characters
#Write a method to check for the presence of character in the string
#Print appropriate messages

class Characters:
    def __init__(self, stringArg, characterArg):
        self.stringArg = stringArg
        self.characterArg = characterArg


    def checkForPresence(self):
        if self.characterArg in self.stringArg:
            return True
        else:
            return False


chk = Characters('Hello', 'a')

if chk.checkForPresence():
    print 'Character is present'
else:
    print 'Character is not present'
