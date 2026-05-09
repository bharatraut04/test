class MAth:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n

    @staticmethod 
    def add(a,b):
        return a + b
    

a = MAth(4)
print(a.num)
a.addtonum(6)
print(a.num) 