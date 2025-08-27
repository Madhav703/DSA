# Program for addition and subtraction of two matrices.

def add_matrices(matrix1, matrix2):
    matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        matrix.append(row)
    return matrix

def subtract_matrices(matrix1, matrix2):
    matrix = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] - matrix2[i][j])
        matrix.append(row)
    return matrix

matrix1 = [[1, 2, 3], [4, 5, 6]]
matrix2 = [[7, 8, 9], [10, 11, 12]]
print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

print("Addition of matrices:")
result_add = add_matrices(matrix1, matrix2)
for row in result_add:
    print(row)

print("Subtraction of matrices:")
result_subtract = subtract_matrices(matrix1, matrix2)
for row in result_subtract:
    print(row)