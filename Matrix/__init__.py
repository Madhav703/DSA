# Addition and Subtraction of two matrix

rows = int(input("Enter the number of rows for the matrix: "))
columns = int(input("Enter the number of columns for the matrix: "))

matrix = []
for m in range(rows):
    row = []
    for _ in range(columns):
        row.append(int(input(f"Enter element at [{m}][{_}]: ")))
    matrix.append(row)
    
print("Matrix:")
for row in matrix:
    print(row)