import pandas as pd 

data = {
    "name" : ['bharat','suresh','raut'],
    "age" : [20,21,33],
    "city" : ['Nagpur','wadsa','desaiganj']
}

df= pd.DataFrame(data)
print(df)

# df.to_csv("output.csv", index = False)
# df.to_excel("output.xlsx", index = False)
df.to_json("output.json", index = False)