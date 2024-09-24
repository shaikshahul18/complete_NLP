def tranpose(matrix):
    row = len(matrix)
    col = len(matrix[0])
    return [matrix[j][i] for i in range(row) for j in range(col)]

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(tranpose(matrix))


print([[j,i] for i in range(3) 
 for j in range(3)
 ])

mat = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(matrix[j][i])
    mat.append(row)
print("here")
for row in mat:
    print(row)
def transpose_matrix(matrix):
    transposed = [[
        matrix[j][i] for j in range(len(matrix))
                   ] 
                   for i in range(len(matrix[0]))
                  ]
    return transposed

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
print("Original matrix:")
for row in matrix:
    print(row)
print("Transposed matrix:")
for row in transposed:
    print(row)

lst = [1,2,3]
print(lst*3)