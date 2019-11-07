#count(x): return the number of times x appears in the list
#index(x, start): return zero-based index in the list of item x
#reverse(): reverse the elements of the list
#append(): add an item to the end of the list
#sort(): sort the item of the list
#pop(i): remove the item at given position in the list and return it. if no index is specified pop removes last item
fruits = ['orange', 'apple', 'pear,', 'banana', 'kiwi', 'apple', 'banana']
#print(fruits.count('apple'))

print(fruits.index('banana'))
print(fruits.index('banana', 4))#find next banana starting a position 4 
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
fruits.pop()
print(fruits)