number = int(input("Enter numbers for the list: "))

list = []

for _ in range(1,number+1):
    n = input(f"Enter number {_}: ")
    list.append(n)

list.sort()
print(f"\nAscending order: {list}")

list.sort(reverse=True)
print(f"Descending order: {list}")
