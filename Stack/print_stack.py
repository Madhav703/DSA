import queue

stack = queue.LifoQueue(maxsize=3)

stack.put('a1')
stack.put('a2')
stack.put('a3')

print("Full: ", stack.full())
print("Size: ", stack.qsize())

print("\nStack contents (top to bottom):")
for item in list(stack.queue):
    print(item)

print("\nStack contents (LIFO order):")
for item in reversed(list(stack.queue)):
    print(item)

print("\nPopping elements from stack:")
while not stack.empty():
    print("Popped:", stack.get())
    print("Remaining size:", stack.qsize())
