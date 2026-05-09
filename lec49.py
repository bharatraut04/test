# class Person :
#     name = "BHArat"
#     occ = "student "

#     def info(self):
#         print(f"{self.name} is a {self.occ}")
# a = Person()
# # a.name = "BHarat Raut"
# # a.occ = "Intern"
# a.info()

## ENCAPSULATION ##

# class Student :
#     __name = "BHArat"

#     def __init__(self):
#         print(self.__name)

#         self.__displayinfo()

#     def __displayinfo(self):
#         print("welcome bro")

# obj=Student()


class MyClass :
    def __init__(self,value):
        self._value = value
    
    def show(self):
        print(f"value is {self._value}")

    @property
    def value(self):
        return self._value
    
obj = MyClass(10)
obj.show()



class MyClass :
    def __init__(self,value):
        self._value = value
    
    def show(self):
        print(f"value is {self._value}")

    @property
    def ten_value(self):             #### GETTER ####
        return 10* self._value
    
    @ten_value.setter
    def ten_value(self,new_value) :    #### SETTER ###
        self._value = new_value/10
    
obj = MyClass(10)
obj.ten_value = 67
print(obj.ten_value) 
obj.show()