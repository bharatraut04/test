a = "bharat bharat bharat"
b = "Bharat!!!!!!"
c = "Bharattttt Sureshhhhhh Rautttttt"
print(a.upper())
print(a.lower())
print(b.rstrip("!"))
print(a.replace("bharat","raut"))
print(c.split(" "))
heading =  "welcome to mY to the chanNel"
print(heading.capitalize())
print(heading.center(60))
print(len(heading.center(60)))
print(a.count("bharat"))
print(b.endswith("!"))
print(heading.endswith("to",4,10)) 
print(heading.find("to"))
print(heading.find("and")) 
print(heading.index("to")) 

reading = "whatisyou"
print(reading.isalnum()) 
reading = "whatisyou000"
print(reading.isalpha()) 

