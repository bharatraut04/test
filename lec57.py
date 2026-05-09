
class parentClass :
    def parent_method (self):
        print("This is the parent method")

class childClass(parentClass):
    def parent_method(self):
        print("BHarat")
        super().parent_method()
    def child_method(self):
        print("This is child method")

        super().parent_method()

child_object = childClass()
child_object.child_method()
child_object.parent_method()
    


class Employee :
    def __init__(self,name,id):
        self.name = name 
        self.id = id
    
class Programmer(Employee) :
    def __init__(self,name,id,lang):
        self.lang = lang 
        super().__init__(name,id)

bharat = Employee("Bharat",21)
raut = Programmer("raut","py",22)
print(bharat.name)
print(raut.name)
print(raut.lang)
print(raut.id)
+y8ywj 02[=41789
4yh2