# Fibonacci: the sum of 2 elements defines next
a, b = 0, 1
while a<10:
    print(a)
    a,b = b, a+b
   # print(a, end=',') # keyword end can be used to avoid newline after output