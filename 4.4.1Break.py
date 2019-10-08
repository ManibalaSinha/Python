
#break statement: breaks out of the innermost enclosing for or while loop.
# Loop statements may have else clause; it is executed when the condition becomes false. else clause belongs to the for loop, not the if
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')


