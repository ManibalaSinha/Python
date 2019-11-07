#tuple: consists of a number of values separated by commas
#tuples are immutable
t = 12345, 543.21, 'hello!'
#t[0]=8888 #you can't change it
u = t, (1,2,3,4,5)

#u =([1.2,2],[3.2,5]) # but they can contain mutable objects

print(u)