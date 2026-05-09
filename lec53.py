class Employee :
    companyName = "Google"
    noOfEmployess = 0
    def __init__(self,name):
        self.name = name 
        self.raise_amount = 0.02
        Employee.noOfEmployess +=1
    def showDetails (self):
        print(f"The name of employee is {self.name } and the raise amount in {self.noOfEmployess} sized {self.companyName } is {self.raise_amount} ")

emp1 = Employee("BHarat")
emp1.raise_amount = 0.035
emp1.showDetails()
# Employee.showDetails(emp1)

emp2 = Employee("Raut")
emp2.showDetails()