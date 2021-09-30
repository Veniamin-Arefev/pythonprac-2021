first_row = list(map(int, input().split(',')))
n = len(first_row)
mat1 = [first_row, *[list(map(int, input().split(','))) for i in range(n - 1)]]
mat2 = [list(map(int, input().split(','))) for i in range(n)]
mat3 = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        for k in range(n):
            mat3[i][j] += mat1[i][k]*mat2[k][j]
# print(mat1)
# print(mat2)
print(*mat3, sep='\n')
