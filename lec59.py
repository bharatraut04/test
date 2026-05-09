class shape : 
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
    
class Circle(shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14 * super().area()
    

# rec = shape(3,4)
# print(rec.area())

c = Circle(5)
print(c.area())



class Employee :
    def salary (self):
        return 20000
    
class Manager(Employee):

    def salary(self):
        base =  super().salary()
        return base + 10000
    
m = Manager()
print(m.salary())



class Animal :
    def speak(self):
        print("Animal makes sound")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog Barks")

d = Dog()
print(d.speak())


class Person:
    def __init__(self,name):
        self.name = name 
        print("Person COnstructor")

class Student(Person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll = roll
        print("Student Constructor")
        print(f"Student name is {self.name} of roll {self.roll}")

s = Student("Bharat",20)