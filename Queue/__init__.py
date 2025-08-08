import queue

stack = queue.LifoQueue(maxsize=3)

stack.put('a1')
stack.put('a2')
stack.put('a3')

print("Full: ", stack.full())
print("Size: ", stack.qsize())
print("Full: ", stack.full())
print("Size, ", stack.qsize())