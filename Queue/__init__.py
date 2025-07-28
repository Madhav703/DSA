from collections import deque
queue = deque()
queue.append(5)
queue.append(7)
queue.popleft()
print(queue[0])
