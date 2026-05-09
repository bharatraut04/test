import  time 

def usingWhile():
    i = 0 
    while i < 200 :
     i = i + 1 
    print(i)
def usingFor():
    for i in range (200) :
        print(i)
  
init = time.time()
usingWhile()
t1 = time.time() - init

init = time.time()
usingFor()
print(time.time()-init)

print(4)
time.sleep(5)
print(" started after 5 sec")

t = time.localtime()
formated_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formated_time)