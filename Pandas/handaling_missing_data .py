import pandas as pd

## detecting MISSING VALUES

# data = {
#     "Name" : ['bharat','suresh', None ,'sangita','gunjan','joe','raj','ram'],
#     "Age" : [21,34,None ,23,23,25,28,31],
#     "Salary" : [50000,23000,None,450000,560000,3400,34500,95000],
#     "Performance Score" : [89,90,None,44,34,97,89,70]
# }
 
# df = pd.DataFrame(data)
# print(df)
# print(df.isnull())
# print(df.isnull().sum) # finds number of missing values 

## Handel the missing value  
  
  #dropping method   

# data = {
#     "Name" : ['bharat','suresh', None ,'sangita','gunjan','joe','raj','ram'],
#     "Age" : [21,34,None ,23,23,25,28,31],
#     "Salary" : [50000,23000,None,450000,560000,3400,34500,95000],
#     "Performance Score" : [89,90,None,44,34,97,89,70]
# }
 
# df = pd.DataFrame(data)
# print(df)

# df.dropna(inplace=True )
# print(df)
    
  #filling method

data = {
    "Name" : ['bharat','suresh', None ,'sangita','gunjan','joe','raj','ram'],
    "Age" : [21,34,None ,23,23,25,28,31],
    "Salary" : [50000,23000,None,450000,560000,3400,34500,95000],
    "Performance Score" : [89,90,None,44,34,97,89,70]
}
 
df = pd.DataFrame(data)
# print(df)


# print("\n filled one")
# df.fillna({
#     "Name": "Unknown",
#     "Age": 0,
#     "Salary": 0,
#     "Performance Score": 0
# }, inplace=True)
# print(df)

## FILLING CALCULATED VALUE 

df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
print(df)
   