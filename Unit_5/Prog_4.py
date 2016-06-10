__author__ = 'Dr.S.Gowrishankar'

import glob, os

directoryPath = raw_input("Enter the directory you want to search")

os.chdir(directoryPath)

for file in glob.glob("*.txt"):
    print(file)

# OR


for file in os.listdir(directoryPath):
    if file.endswith(".txt"):
        print(file)
