#when looping through dictionaries, the key and corresponding value can be retrieved at the same time using items() method
#when looping through a sequence, the position index and corresponding value can be retrieved at the same time using enumerate() function

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)   
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)
    
