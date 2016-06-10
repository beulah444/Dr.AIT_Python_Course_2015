__author__ = 'Dr.S.Gowrishankar'


#write the output for the following program

#Variable declaration
i = 1
j = 1

#while loops
while i <= 5: #outer loop
    i = i+1
    while j <= 5: #inner loop
        j = j+1
        if j == 5:
            break #break statement in inner loop
        else:
            print i, j
