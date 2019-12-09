#Formatted string literals let you include {expression} inside string by prefixing string with f
import math
print(f'The value of pi is approximately {math.pi:.3f}')
#passing an integer after ":" will cause field to be minimum number of characters wide.
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')