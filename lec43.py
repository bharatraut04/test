# # seek()
# with open('myfile.text','r') as f:

#     f.seek(10)

#     data = f.read(2)
#     print(data)

# # tell()  
# with open('myfile.text','r') as f:

#     f.seek(10)

#     print(f.tell())

#     data = f.read(5)
#     print(data)

# truncate()
with open('myfile.text','w') as f:
    f.write("Hello World")
    f.truncate(9)

