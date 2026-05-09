#MAP
def cube(x):
    return x*x*x 

print(cube(2))


l = [1,2,3,4,5]
# newl = []

# for iteam in l :
#     newl.append(cube(iteam))

newl = list(map(cube,l))    
print(newl)

#FILTER
def filter_funcation(a):
    return a>2

newnewl = list(filter(filter_funcation,l))
print(newnewl)

from functools import reduce

number = [1,2,3,4,5]

sum  = reduce(lambda x,y : x + y , number  )
print(sum)