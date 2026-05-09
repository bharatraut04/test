class Animal :
    def __init__(self,name,species):
        self.name =  name 
        self.species = species

    def show_details(self):
        print(f"name:{self.name}")
        print(f"Species:{self.species}")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        self.breed = breed

    def show_details(self):
        Animal.show_details(self)
        print(f"Breed:{self.breed}")

class GoldenRetrivar(Dog):
    def __init__(self, name, color):
        Dog.__init__(self,name, breed = "GoldenRetrivar")
        self.color = color

    def show_details(self):
        Dog.show_details(self)
        print(f"color={self.color}")

obj = GoldenRetrivar("Bruno","Brown")
print(obj.show_details())