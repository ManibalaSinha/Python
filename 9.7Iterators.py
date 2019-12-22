#for statement calls iter() on container object
"""for element in [1, 2, 3]:
    print(element)
for key in {'one':1, 'two':2}:
    print(key)
for char in "123":
    print(char)"""
 
#next() method: accesses elements in container one at a time
#When there are no more elements, __next__() raises StopIteration exception which tells the for loop to terminate. 
"""s = 'abc'
it = iter(s)

print(next(it)) #'a'
print(next(it)) #'b'

print(next(it)) #c 
print(next(it))"""
#When there are no more elements, __next__() raises a StopIteration exception which tells the for loop to terminate. 
class Reverse:
    
    def __init__(self, data): #often 1st argument of a method is called self
        self.data = data
        self.index = len(data)

    def __iter__(self):#Iterator for looping over a sequence backwards
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
print(iter(rev))
for char in rev:
    print(char) 