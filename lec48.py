class Person :
    name = "BHArat"
    occ = "student "

    def info(self):
        print(f"{self.name} is a {self.occ}")
a = Person()
a.name = "BHarat Raut"
a.occ = "Intern"
a.info()

## CONSTRUCTORS ##

class Person :
    def __init__(self,n,o):
        print("hey i am perosn")
        self.name = n
        self.occ = o

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Bharat","Student")
b = Person("Raut","Intern")
a.info()
b.info()


## DECORATORS ##

def greet(fx):
    def mfx(*args,**Kwargs):
        print("Good Morning")
        fx(*args,**Kwargs)
        print("Thanks for using")
    return mfx

@greet
def hello():
    print("hello world")


# @greet
# def add(a,b):
#     print(a+b)

hello()
# add(1,2)

# import logging

# def log_function_call(func):
#     def decorated(*args,**kwargs):
#         logging.info(f"calling{func.__name__} with args={args}, kwargs={kwargs}")
#         result = func(*args,**kwargs)
#         logging.info(f"{func.__name__} returned {result}")

#         return result
    # return decorated