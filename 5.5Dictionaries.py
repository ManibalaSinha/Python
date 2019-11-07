#dictionaries are set of key: value pairs. 
#used for storing a value with some key and extracting the value given the key. 
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
#print(tel)
#print(tel['jack'])
del tel['sape']
tel['irv'] =4127
#print(tel)
#print(list(tel))# list shows key 
print(sorted(tel))# sorted list
x = {x: x**2 for x in (2,4,6)}
#print(x)
