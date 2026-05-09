# reading #
# f = open('myfile.text','r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# # writting 
# f = open('myfile.text','w')
# f.write("hello,world")
# f.close()

#append
f = open('myfile.text','a')
f.write("hello,world weklcome to here")
f.close()

with open('myfile.text','a')as f:
    f.write("i am inside")