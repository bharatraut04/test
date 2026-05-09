class Animal :
    def __init__(self,name , species):
        self.name = name 
        self.species = species
    
    def make_sound(self):
        print("Sound made by the animal")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species = "Dog")
        self.breed = breed

    def make_sound(self):
        print("Bhauuuu!!!!")


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species = "Dog")
        self.breed = breed

    def make_sound(self):
        print("MEOWWWWWWWW!!!!")


a = Animal("Dog","Dog")
a.make_sound()

d = Dog("Bruno","Pug")
d.make_sound()

c = Cat("pussy","indie")
c.make_sound()