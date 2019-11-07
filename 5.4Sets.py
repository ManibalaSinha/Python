#Set: is an unordered collection with no duplicate elements.
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket) # shows duplicates have been removed and not in alphabetical order
print('orange' in basket)
print('crabgrass' in basket)
a = set('abracadabra')
b = set('alacazam')
print(a)# print unique letters in a
print(a-b)# print letters in a but not in b
print(a|b)# print letters in a or b or both
print(a&b)# letters in both a and b
print(a^b)# ^exclusive-or(bitwise) letters in a or b but not both
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)