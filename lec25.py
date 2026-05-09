letter = "hey my is {1} and i live in {0}"
name = "bharat"
country = "India"

print(letter.format(country,name)) #old method 
print(f"hey my is {name} and i live in {country}") # new method
#print(f"hey my is {{name}} and i live in {{country}}") # new method

price = 56.9874123
print(f"the bus fare cost me {price:.2f}")