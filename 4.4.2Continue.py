#continue: continues with next iteration of loop.
for num in range(2,10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found a odd number", num)