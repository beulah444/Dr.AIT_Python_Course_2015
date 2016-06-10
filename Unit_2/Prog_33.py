__author__ = 'Dr.S.Gowrishankar'

#Program to add two matrices using nested loops

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]


result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

#iterate through rows
for i in range(len(x)):
    #iterate through columns
    for j in range(len(y[0])):
        result[i][j] = x[i][j] + y [i][j]

#print the resultant matrix

for r in result:
    print r


