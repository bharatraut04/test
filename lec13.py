# time = float(input("Enter the time: "))
# if(time<12 and time>6):
#     print("Good Morning")
# elif(time>12 and time<16):
#     print("Good Afternoon")
# elif(time>16 and time < 23):
#     print("Good Evening")
# else:
#     print("enter a valid time")

import time
t = time.strftime('%H:%M:%S')
hour  = int(time.strftime('%H'))
print(hour)

if(hour>=0 and hour<12):
    print("Good Morning")
elif(hour>=12 and hour<16):
    print("Good Afternoon")
elif(hour>=16 and hour < 23):
    print("Good Evening")