import array

arr = array.array('i', [1, 2, 3, 4, 5])

number = int(input("Enter a number: "))
if number in arr:
    print("Item found")
else:
    print("Item not found")