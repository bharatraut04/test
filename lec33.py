try:
    l = [1,2,3,4]
    i = int(input("enter the  index value "))
    print(l[i])
except:
    print("error occured")


finally:
    print("i am always run")



def funct2():

    try:
     l = [1,2,3,4]
     i = int(input("enter the  index value "))
     print(l[i])
     return 1
    except:
     print("error occured")
     return 0

    finally:
     print("i am always run")

x = funct2()
print(x)    


def funct2():

    try:
     l = [1,2,3,4]
     i = int(input("enter the  index value "))
     print(l[i])
    except:
     print("error occured")


    
     print("i am always run")
     
x = funct2()
print(x) 