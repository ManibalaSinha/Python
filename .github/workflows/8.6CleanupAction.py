#finally clause: will execute as the last task before try statement completes.
#finally clause runs whether or not try statement produces an exception.
#if the exception is not handled by except clause, exception is reraised after finally has been executed
#if finally includes return statement, finally will execute before return statement in try clause
def bool_return():
    try:
        return True
    finally:
        return False
print(bool_return()) 