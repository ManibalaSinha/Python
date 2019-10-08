# to modify the sequence you are iterating over while inside for loop
#  it is recommented that you first make a copy.
# loop over a slice copy of the entire list.
# insert(index, element) method: inserts an element to the list at a given index.
words = ['cat', 'window', 'differentiate']
 
for w in words[:]:
     if len(w) > 6:
         words.insert(0,w)
         print(w)
         print(words)
         