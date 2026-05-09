# class Employee :
#     def __init__(self):
#         self.name = "Bharat"

# a = Employee()
# print(a.name)

# ## PRIVATE ACCESS MODIFIER ##

# class Employee :
#     def __init__(self):
#         self.__name = "Bharat"

# a = Employee()
# print(a._Employee__name)

## PROTECTED ACCESS MODIFIER ##

class Student :
    def __init__(self):
        self._name = "Bharat"

    def _funName(self):
        return "Raut"

class Subject(Student):
    pass

obj = Student()
obj1 = Subject()

print(obj._name)
print(obj._funName())


print(obj1._name)
print(obj1._funName())