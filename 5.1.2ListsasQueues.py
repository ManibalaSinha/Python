#Queue:(first-in, first-out)where the first element added is the first element retrived
#To implement queue, use collections.deque which was designed to have fast appends and pops from both ends
from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")
queue.append("Graham")
queue.popleft()
queue.pop()
print(queue)
