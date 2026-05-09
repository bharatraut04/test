#break statement 
for i in range(1,15):
    if (i == 10):
        break
    print("5 X",i,"=", 5 * i) 
print("i am free")


#continue statement 

for i in range(1,15):
    if (i == 10):
        print("10 is skiped")
        continue
    print("5 X",i,"=", 5 * i) 

