#generators can be coded as expressions using a syntax similar to list comprehensions
#but with parentheses instead of square brackets.
print(sum(i*i for i in range(10)))                 # sum of squares

xvec = [10, 20, 30]
yvec = [7, 5, 3]
#zip() function creates iterator that will aggregate elements from 2 or more iterables 
print(sum(x*y for x,y in zip(xvec, yvec)))         # dot product

data = 'golf'
print(list(data[i] for i in range(len(data)-1, -1, -1)))