#double underscore __prefixed to a variable makes it private.Any attempt to do shows AttributeError
class employee:
    def __init__(self, name, sal):
        self.__name=name  # private attribute 
        self.__salary=sal # private attribute
e1=employee("Bill", 10000)
print(e1.__salary) # cant access private salary shows AttributeError
#every member with double underscore will be changed to obj._class__variable
#print(e1._employee__salary) 