import pandas as pd

## COLUMN MODIFICATION ##
data = {
    "Name" : ['bharat','suresh','raut','sangita','gunjan','joe','raj','ram'],
    "Age" : [21,34,56,23,23,25,28,31],
    "Salary" : [50000,23000,120000,450000,560000,3400,34500,95000],
    "Performance Score" : [89,90,65,44,34,97,89,70]
}
 
df = pd.DataFrame(data)
print(df)
# # using assign

# df["Bonus"] = df['Salary'] * 0.1
# print(df)

# # using INSERT {}
# df.insert(0,"Employee Id",[10,20,30,40,50,60,70,80])
# print(df)

# Updating  ROW Values using .loc[]
 
# df.loc[0,"Salary"] = 55000
# print(df)

# UPdating whole column
# df['Salary'] = df['Salary']* 1.05
# print(df)

# Removing ROW & COLUMNS

# df.drop(columns=["Performance Score"],inplace = True)
# print(df)

df.drop(columns=["Performance Score","Age"],inplace = True)
print(df)
