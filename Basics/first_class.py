class Person :
    def show(self):
        print("show in person")
        
class Human :
    def show(self):
        print("show in Human")
        
class Employee(Person,Human):
    
    """This is Employee class (will
    only display if put at first)"""

    cname ="Accenture"
    
    def __init__(self,eid ,name):
        print("inside init")
        self.__empid = eid
        self.__empname = name
        print(self.__empid,"    ",self.__empname)

    
    def info(self):
        super().show()   #to access parent class
        print(self.__empid)
        
    def show(self): # this is overriding but overloading is not supported
        print(self.__empid)  
    
print(Employee.__doc__)
print(Employee.cname)
obj=Employee(101,"sam")
#print(obj.__empid,"    ",obj.__empname)  
#__ is used to make function private
print(obj.info())
obj.show()