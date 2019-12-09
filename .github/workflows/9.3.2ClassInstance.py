#class defines __init__() method, class instantiation invokes __init__()
class Dog:
    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):#often 1st argument of a method is called self
        self.name = name    # instance variable unique to each instance

d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)   #canine            # shared by all dogs

print(e.kind)   #canine            # shared by all dogs

print(d.name)   #Fido              # unique to d

print(e.name)   #Buddy             # unique to e
