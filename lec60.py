# class vector :
#     def __init__(self,i,j,k):
#         self.i = i
#         self.j = j
#         self.k = k

#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k "
#     def __add__(self, x):
#         return vector(self.i + x.i , self.j + x.j, self.k + x.k )
# v1 = vector(1,2,3)
# print(v1)

# v2 = vector(12,42,36)
# print(v2)

# print(v1 + v2)
# print(type(v1 + v2))


## STRING JOINING ##

class word:
    def __init__(self,text):
        self.text = text
    
    def __add__(self, other):
        return self.text+" "+other.text
    
w1 = word("Bharat")
w2 = word("Raut")
print(w1+w2)


## COMPARING OBJECTS ##

class students :
    def __init__(self,marks):
        self.marks = marks 

    def __gt__(self, other):
        return self.marks > other.marks 
    
s1 = students(21)
s2 = students(24)

print(s1 > s2)