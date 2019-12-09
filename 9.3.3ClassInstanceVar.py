class Dog:
    def __init__(self, name):#often 1st argument of a method is called self
        self.name = name
        self.tricks = [] #create a empty list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)
print(e.tricks)  
print(e.name)