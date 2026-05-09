# # participent = input("Enter Your name ")
# # print("Welcomm ",participent," to Kaun Banega Crorepati (KBC) ")
# # print("hope u r doing well ")
# # print("chalo shrur krte hai Kaun Banega Crorepati (KBC) ")
# # print("ye rha tv screen pe pehela sawal 1k ke liye")
# print("Question 1 = What comes after b")
# print("apke option hai (a)E (B)T (C)C (D)Z")
# answer = input("write your answer here :")
# a = "E"
# b = "T"
# c = "C" 
# d = "z"

# if( answer.upper() ==c ):
#     print("sahi answer aap win krte ho 1k ")
#     print("total amount win = 1k ")
#     #second question
#     print("ye rha tv screen pe dusra sawal 2k ke liye")
#     print("Question 2 = national animal")
#     print("options are : (A)Lion , (B)Tiger, (C)Hen, (D)Dog")
#     answer = input("write your answer here :")
#     a = "Lion"
#     b = "Tiger"
#     c = "Hen" 
#     d = "Dog"
#     if( answer.upper()== "B" ):
#         print("sahi answer apke khate me 2k jate huye ")
#         print("total amount win = 3k ")
#     else :
#          print("ummmm.......galat uttar")
#          print("Balance : 00000")

# else :
#     print("ummmm.......galat uttar")
#     print("winning Balance = 0000000")
#     print("Ghar ja skte ho")



print("Welcome to Kaun Banega Crorepati")
print("Aapka swagat hai hot seat par!\n")

money = 0

# Question 1
print("Question 1 (₹1,000)")
print("What comes after B?")
print("A. E   B. T   C. C   D. Z")

answer = input("Lock kiya jaye? (Enter option): ")

if answer.upper() == "C":
    money = 1000
    print("Sahi jawab! Aap jeet gaye ₹1,000\n")
else:
    print("Galat jawab! Aap ghar ja sakte hain.")
    print("Winning Amount: ₹0")
    exit()

# Question 2
print("Question 2 (₹2,000)")
print("National Animal of India?")
print("A. Lion   B. Tiger   C. Hen   D. Dog")

answer = input("Lock kiya jaye? (Enter option): ")

if answer.upper() == "B":
    money = 3000
    print("Sahi jawab! Total jeet: ₹3,000\n")
else:
    print("Galat jawab!")
    print(f"Winning Amount: ₹{money}")
    exit()

# Question 3
print("Question 3 (₹5,000)")
print("Which language is used for Data Science?")
print("A. Python   B. HTML   C. CSS   D. Paint")

answer = input("Lock kiya jaye? (Enter option): ")

if answer.upper() == "A":
    money = 8000
    print("Sahi jawab! Total jeet: ₹8,000\n")
else:
    print("Galat jawab!")
    print(f"Winning Amount: ₹{money}")
    exit()



print("\nGame Over!")