# a= True
# print(a:=False)

number = [1,2,3,4,5]

while (n:= len(number)) > 0 :
    print(number.pop())

names = ["bharat","suresh","raut"]

if (name := input("ENter a name : ")) in names:
    print(f"hello,{name}")
else :
    print("name not found")

# foods = list()
# while True :
#     food = input("Enter the food you like :")
#     if food == "quit":
#         break 
#     foods.append(food)


foods = list()
while (food := input("Enter the food you like :")) != "quit":
    foods.append(food)