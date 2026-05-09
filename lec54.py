# class Employee :
#     company = "Apple"
#     def show(self):
#         print(f"the name is {self.name} and company is {self.company}")

#     @classmethod
#     def changeCompany(cls , newCompany):
#         cls.company = newCompany

# e1 = Employee()
# e1.name = "BHarat"
# e1.show()
# e1.changeCompany("TATA")
# e1.show()
# print(Employee.company)


class exampleClass :
    @classmethod
    def factory_method(cls, argument1,argument2):
        return cls(argument1,argument2)