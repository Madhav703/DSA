# Addition and Subtraction of two matrix

def input_matrix(rows, cols, name="Matrix"):
    print(f"Enter elements of {name}:")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        matrix.append(row)
    return matrix

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def subtract_matrices(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def print_matrix(matrix, name="Result"):
    print(f"{name}:")
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    A = input_matrix(rows, cols, "Matrix A")
    B = input_matrix(rows, cols, "Matrix B")

    sum_matrix = add_matrices(A, B)
    diff_matrix = subtract_matrices(A, B)

    print_matrix(sum_matrix, "Addition")
    print_matrix(diff_matrix, "Subtraction")