#Class objects support 2 kinds of operations: attribute references and instantiation
#Attribute references use standard syntax: obj.name
#Class instantiation uses function notation. ex: x= MyClass()
class MyClass:
    i = 12345

    def f(self): #parameterless function
        return 'hello world' #return function object and creates empty object
        
print(MyClass.f) #attribute references
print(MyClass.i) #attribute references
x=MyClass() #instantiation
print(x) #returns new instance of the class that creates empty object
#class defines __init__() method, class instantiation invokes __init__() 
def __init__(self): #__init__() method may have arguments for greater flexibility
    self.data = [] #creating empty list for MyClass
