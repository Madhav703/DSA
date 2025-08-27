n = []

m = [1, 2, 3,]
m2 = [6, 7, 8, ]
m3 = [9, 10, 11]

n.append(m)
n.append(m2)   
n.append(m3)

for m in range(len(n)):
    for j in range(len(n[m])):
        print(n[m][j], end=" ")
    print()