#Last-In/First-Out (LIFO) or First-In/Last-Out (FILO)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)
#Deletes the topmost element of the stack 
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)
stack.append(21)
stack.append(22)
stack.append(23)

print(stack.push())
print(stack.push())
print(stack.push())
