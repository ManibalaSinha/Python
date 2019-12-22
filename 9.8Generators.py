#Generators are a simple and powerful tool for creating iterators.
#it's like regular functions but use the yield statement whenever they want to return data.
#Each time next() is called on it,the generator resumes where it left off
def reverse(data):
    for index in range(len(data)-1, -1, -1): #range(start,stop,step)
        yield data[index]
for char in reverse('golf'):
    print(char)