#try clause is executed between try and except keywords  
while True:
    try:
        x = int(input("Please enter a number: "))
        break # check out without interruption
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")