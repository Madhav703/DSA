a = [1, 2, 3]
b = [2,5, 6]

add = [0,0,0]
sub = [0,0,0]

for i in range(2):
    for j in range(2):
        add[i][j] = a[i][j] + b[i][j]

for i in range(2):
    for j in range(2):
        sub[i][j] = a[i][j] - b[i][j]

# Addition
print("Addition")
for i in add:
    print(i)

# Subtraction
print("Subtraction")
for i in sub:
    print(i)

