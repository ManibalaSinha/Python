#Default argument vlaues:specify default value for one or more arguments.
#creates function with fewer arguments
i = 5
def f(arg=i):
    arg=6
    print(arg)
f()












#in keyword: this tests whether or not a sequence contains a certain value.
""" def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries -1
        if retries < 0:
            raise ValueError('invalid your response')
        print(reminder) """