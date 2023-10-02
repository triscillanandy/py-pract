# Initializing a queue
queue = []

# Adding elements to the queue
queue.append('e')
queue.append('f')
queue.append('g')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.pop(0))
print(queue.pop(0))

print(queue.pop(0))

print("\nQueue after removing elements")
print(queue)

from collections import deque

queue = deque()
queue.append('e')
queue.append('f')
queue.append('g')

print("Initial queue")
print(queue)

# Removing elements from the queue
print("\nElements dequeued from queue")
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())

print("\nQueue after removing elements")
print(queue)

