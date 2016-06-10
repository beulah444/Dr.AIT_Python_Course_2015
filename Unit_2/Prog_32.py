__author__ = 'Dr.S.Gowrishankar'

# program to multiply two matrices using nested loops

x = [[1,2,3],
     [4,5,6],
     [7,8,9]]

y = [[1,2,3],
     [4,5,6],
     [7,8,9]]

#use the below y and result values if you want to compute
# 3 x 4 matrices
# y = [[1,2,3,8],
#      [4,5,6,8],
#      [7,8,9,8]]

# result = [[0,0,0,0],
#           [0,0,0,0],
#           [0,0,0,0]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

#iterate through all the rows of x
for i in range(len(x)):
    #iterate through the columns of y
    #give special attention here its len(y[0]) and not len(y)
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]

#print the resultant matrix
for r in result:
    print r



