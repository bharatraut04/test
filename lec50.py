class Employee :
    def __init__(self,name,id):
        self.name = name 
        self.id = id
    
    def showDetails(self):
        print(f"the name of Employee : {self.id} is {self.name}")

class Programmer(Employee):
    def showLanguage(self):
        print("default lang is PYTHON")

e1 = Employee("Bharat", 4)
e1.showDetails()
e2 = Programmer("Raut", 40)
e2.showDetails()
e2.showLanguage()
