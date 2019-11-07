#anonymous functions can be created with lambda keyword.
#Lambda functions can be used where functions objects are required. 
def make_incrementor(n):
    return lambda x: x + n
f = make_incrementor(42)
#use as anonymous function inside another function
print(f(1))