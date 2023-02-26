p = int(input('Enter number of rows. : \n'))
q = int(input('Enter number of cols. : \n'))
n = int(input('Enter number of rows for matrix1 and cols for matrix2  : \n'))

print('Enter elements for first matrix. : \n')

matrix1 = [[int(input()) for i in range(n)] for j in range(p)]
print('matrix1 : \n',matrix1)


print('Enter elements for second matrix. : \n')

matrix2 = [[int(input()) for i in range(q)] for j in range(n)]
print('matrix2 : \n',matrix2)



     
result = [[0 for i in range(q)] for j in range(p)]

for i in range(p):
    for j in range(q):
        for k in range(n):
            result[i][j]  =  result[i][j] + matrix1[i][k] * matrix2[k][j]

print('\nresult : \n',result)
