__author__ = 'Dr.S.Gowrishankar'

#Program to find the transpose of a matrix

x = [[12,7],
     [4,5],
     [3,8]]

result = [[0,0,0],
          [0,0,0]]

#iterate through rows

for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i] = x[i][j]

for r in result:
    print r


