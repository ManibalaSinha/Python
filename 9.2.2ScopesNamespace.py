#namespace: is mapping from names to objects.ie built-in names ex: abs(), global name in module, local name in function invocation
#if we make any changes inside the nested function, the changes appears outside the local scope, i.e scope_test().
def scope_test():
    def do_local():
        #it takes previous value
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam # takes previous value here
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)