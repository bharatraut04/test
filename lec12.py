a = int(input("enter your age: "))
print("your age is ",a)

#conditional operator
#     >,<,<=,>=,==,!=

print(a>18)
print(a<18)
print(a>=18)
print(a<=18)
print(a==18)
print(a!=18)

if(a>18):
    print("you can drive")
else:
    print("you can't drive")

if(a<0):
    print("Number is negative")
elif(a>0):
    if(a <= 10 ):
        print("number is betn 1-10")
    elif(a >= 10 and a<=20):
        print("number is betn 10-20")
    else:
        print("number is above 20")    
else:
    print("number is positive")