x = int(input("enter the value of X : "))

match x :

    case 0 :
        print("X is zero")

    case 4:
        print("x is 4")
    
    case _ if (x != 90):
        print(x,"is not 90")
    case _ if (x != 80):
        print(x,"is not 80")
    case _ if (x != 70):
        print(x,"isn not 70")
        