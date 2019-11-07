# to unpack for a function call separate arguments.
#  * operator are used to unpack the arguments out of list or tuple.
list(range(3,6)) #3,4,5
args = [3,6] # separate arguments
print(list(range(*args))) # * operator to unpack the argument
