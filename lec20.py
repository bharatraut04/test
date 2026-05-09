# marks = [3,5,8,"Bharat",True]
# print(marks)
# print(marks[0]) #positive indexing 
# print(marks[1])
# print(marks[-2]) #negative indexing 

# print(marks[len(marks)-3]) #simple hack for finding negative index 

# if -2 in marks:
#     print("yes")
# else:
#     print("no")

# if "Bharat" in marks:
#     print("yes")
# else:
#     print("no")

# if "arat" in "bharat":
#     print("yes")
# else:
#     print("no")

# list = [1,4,"rt","yh","fdgdgsr","sdsg","sdgsg",5555,35654,"dgesgseges", "sdvs55","786sds132"] 
# print(len(list))
# print(list[:])
# print(list[0:11:2])

# list comprehension

# lst = [i for i in range(10)]
# print(lst)

# lst = [i*i for i in range(10)]
# print(lst)

# lst = [i*i for i in range(10) if i%2==0]
# print(lst)

lst = ["bharat","Suresh","raut","yash","pant","Cats"]
namewithR = [i for i in lst if "r" in i]
print(namewithR)

nameWithletters = [i for i in lst if (len(i)<= 4)]
print(nameWithletters)

nameWithoutT = [i for i in lst if "t" not in i] 
print(nameWithoutT)
