import os
from os.path import join

userPath = raw_input("Enter the Path of the directory where text files are stored")
for (dirname, dirs, files) in os.walk(userPath):
    for filename in files:
        if filename.endswith('.txt'): #change this if asked for other kind of extensions like .mp3, .mpeg, .jpeg, .png
            thefile = os.path.join(dirname,filename)
            #If you want to print size and Entire path of the file
            print os.path.getsize(thefile), thefile
            #If you want to print only the path
            print thefile