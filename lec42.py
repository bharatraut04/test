# readline method
# f = open('myfile2.text','r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

# f = open('myfile3.txt','r')
# i =0
# while True:
#     i = i + 1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"marks of student {i} in maths is : {m1}")
#     print(f"marks of student {i} in gk is : {m2}")
#     print(f"marks of student {i} in sst is : {m3}")

#     print(line)


# writeline method()

# f = open('myfile2.text','w')
# line = ('line 1\n','line 2\n','line 3\n')
# f.writelines(line)
# f.close

with open('myfile2.text','w') as f:
    for i in range(1,66):
        f.write(f"line {i}\n")


