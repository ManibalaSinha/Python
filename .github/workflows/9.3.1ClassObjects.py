#__init__() method may have arguments for greater flexibility
class Complex:
    def __init__(self, realpart, imagpart):#often 1st argument of a method is called self
        self.r = realpart
        self.i = imagpart
x= Complex(3.0,-4.7)
print(x.r, x.i)