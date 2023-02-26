row = int(input('Enter number of rows. : \n'))
col = int(input('Enter number of cols. : \n'))

print('Enter elements for first matrix. : \n')
matrix1 = [[int(input()) for i in range(row)] for j in range(col)]
print('matrix1 : \n',matrix1)

print('Enter elements for second matrix. : \n')
matrix2 = [[int(input()) for i in range(row)] for j in range(col)]
print('matrix2 : \n',matrix2)

result = [[0 for i in range(row)] for j in range(col)]
for i in range(col):
    for j in range(row):
        result[i][j] = matrix1[i][j] + matrix2[i][j]


print('result : \n',result)
        
