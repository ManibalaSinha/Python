#class inheritance mechanism allows multiple base or super classes, a derived class can override
#isinstance() to check an instance’s type: isinstance(obj, int) will be True only if obj.__class__ is int or some class derived from int.
#issubclass() to check class inheritance: issubclass(bool, int) is True since bool is a subclass of int. However, issubclass(float, int) is False since float is not a subclass of int.
class Base1: 
	def __init__(self): 
		self.str1 = "Geek1"
		print(Base1)

class Base2: 
	def __init__(self): 
		self.str2 = "Geek2"		
		print(Base2)

class Derived(Base1, Base2): 
	def __init__(self): 
		
		# Calling constructors of Base1 and Base2 classes 
		Base1.__init__(self) 
		Base2.__init__(self) 
		print(Derived)
		
	def printStrs(self): 
		print(self.str1, self.str2, sep=",") 
		

ob = Derived() 
ob.printStrs() 
