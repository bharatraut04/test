# a = input("Enter the number :")
# print(f"multiplicatio of {a} is :")
# try:
#     for i in range(1, 11):
#          print(f"{int(a)} X {i}={int(a)*i}")
# except:
#      print("INPUT ERROR!!!!!")

# print("hello")
# print("mrs.")


try:
     num = int(input("ENter the value :"))
     a = [4, 8]
     print(a[num])
except ValueError:
     print("number is not interger")
except IndexError:
     print("index error")     
