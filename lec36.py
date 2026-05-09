marks = [22,33,44,55,97,3,2,6,7]

# index  = 0 
# for mark in marks:
#     print(mark)             this is what useally we do
#     if (index == 4):
#         print("nice marks ")
#     index +=1


# for index, mark in enumerate(marks):
#     print(mark)              # trick to do it 
#     if(index == 4):
#         print("nimce marks")

for index, mark in enumerate(marks,start=0):
    print(mark)              # trick to do it 
    if(index == 4):
        print("nimce marks")   