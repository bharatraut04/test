class Person :
    def __init__(self,name,age):
        self.name = name 
        self.age = age 
    
    @classmethod
    def from_str(cls,string):
        name,age = string.split(',')
        return cls(name,int(age))

Person = Person.from_str("bharat,21")
print(Person.name, Person.age)



class Rectangle :
    def __init__(self,width,height):
        self.width = width
        self.height = height 

    @classmethod
    def square(cls,size):
        return cls(size,size)
    
rec = Rectangle.square(10)
print(rec.width , rec.height)





class Employee :
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls,string) :
        name , salary = string.split("-")
        return cls(name,int(salary))

e1 = Employee("Bharat",12000)
print(e1.name)
print(e1.salary)

string = "Raut-10000"
e2 = Employee.fromstr(string)
print(e2.name)
print(e2.salary)
