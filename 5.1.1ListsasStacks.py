#Stack: (last-in, first-out)where the last element is added is the first element retrieved.
#To add an item to the top of stack, use append().To retrieve an item from the top of stack, use pop()
stack = [3, 4, 5] 
stack.append(6)
stack.append(7)
print(stack)
stack.pop()
stack.pop(3)
print(stack)