class Person :
    name = "Harry"
    occupation = "Student"
    networth = 0

    def info(self) :
        print(f"{self.name} is a {self.occupation}")

a = Person()
b = Person()
a.name = "Bharat"
a.occupation = "intern"
b.name = "raut"
b.occupation = "HR"

print(a.name,a.occupation)
a.info()
b.info()
