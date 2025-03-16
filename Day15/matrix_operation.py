matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
matrix2 = [[1,1,1],[2,2,2],[3,3,3]]
print('Example matrices: ')
for i in range(len(matrix1)):
    print(matrix1[i],end=' ')
    print(matrix2[i],end=' ')
    print()
print()

print('Addition of two matrices: ')
for i in range(len(matrix1)):
     for j in range(len(matrix1[i])):
        matrix1[i][j] = matrix1[i][j] + matrix2[i][j]
        print(matrix1[i][j],end=' ')
     print()
print()  


print('matrix1 diagonal elements: ')
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix1)):
     for j in range(len(matrix1[i])):
        #  if i==j:
        #      print(matrix1[i][j],end=' ')
        #  else:
        #      print(' ',end=' ')
         if i==j or i+j == len(matrix1)-1:
             print(matrix1[i][j],end=' ')
         else:
             print(' ',end=' ')
     print()
print()


print('matrix2 diagonal elements: ')
matrix2 = [[1,1,1],[2,2,2],[3,3,3]]
for i in range(len(matrix2)):
    for j in range(len(matrix2[i])):
        # if i==j:
        #      print(matrix2[i][j],end=' ')
        # else:
        #      print(' ',end=' ')
        if i==j or i+j == len(matrix2)-1:
            print(matrix2[i][j],end=' ')
        else:
            print(' ',end=' ')
    print()
print()


print('product of two matrices: ')
result = [[0,0,0],[0,0,0],[0,0,0]]
if len(matrix1[0]) != len(matrix2):
    print('Invalid matrix')
for i in range(len(matrix1)):
    for j in range(len(matrix2)):
        for k in range(len(matrix2)):
             result[i][j] += matrix1[i][k] * matrix2[k][j]
for i in range(len(result)):
     for j in range(len(result[i])):
        print(result[i][j],end=' ')
     print()