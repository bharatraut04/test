## Dir ##

# x = [1,2,3]
# print(dir(x))
# print(x.__add__)
# print(x.append)

## dict ##

class person :
    def __init__(self,name,age):
        self.name  = name 
        self.age = age 

p = person("BHarat",21)
print(p.__dict__)

print(help(person))    ## help() ##

