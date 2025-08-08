stack = []

items = int(input("Enter the number for the list: "))

for _ in range(1,items+1):
    number = int(input("Enter number {}: ".format(_)))
    stack.append(number)
    
print(f"\nOriginal list: {stack}")    
print(f"Number {stack[-1]} popped out from the list as it was the last number in the list.")
stack.pop()
print(f"New list: {stack}")