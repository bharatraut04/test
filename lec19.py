#default argument 

# def average(a, b):
#     print("print the average of",(a+b)/2)

# average(4, 6)

# def name(fname, mname = "suresh", lname="Raut"):
#     print("hello",fname,mname,lname)
# name("bharat","sangita")

#keyword argument 

# average(b=9,a=6)

#variable length Argument 

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum +i
    print("average is:",sum / len(numbers))    

average(7, 3)
