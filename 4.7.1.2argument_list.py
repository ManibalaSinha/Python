#return:statement causes your function to exit and hand back a value to its caller.
def f(a, L=[]):
    L.append(a)
    return L
print(f(1))
#print(f(2))
print(f(3))