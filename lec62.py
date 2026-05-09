class Employee :
    def __init__(self,name):
        self.name = name

    def show(self):
        print(f"the name is {self.name}") 

class Dancer :
    def __init__(self,dance):
        self.dance = dance 
    def show (self):
        print(f"the dance is {self.dance}")   

class DancerEmployee(Employee, Dancer):
    def __init__(self, name,dance):
        self.name = name 
        self.dance = dance 

o = DancerEmployee("BHarat","POP")
print(o.name)
print(o.dance)
o.show()
# print(DancerEmployee.mro())



class A :
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()
        print("B")
    
class C(B):
    def show(self):
        super().show()
        print("C")

obj = C()
obj.show()
