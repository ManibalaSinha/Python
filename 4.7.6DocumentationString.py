# we write the document inside function and call the function by functionname.__doc__
def my_function():
    """ Do nothing, but document it

    It doesn't do anything.
    """
    pass
print(my_function.__doc__)