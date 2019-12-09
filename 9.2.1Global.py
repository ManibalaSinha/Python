#we can only access global variable but cannot modify it from inside the function.
c=1 #global variable
def add():
    global c
    c=c+2
    print(c)
add()