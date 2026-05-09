import pandas as pd

data = {
    "Name" : ['bharat','suresh', 'raut' ,'sangita','gunjan','joe','raj','ram'],
    "Age" : [21,34,None ,23,23,25,28,31],
    "Salary" : [50000,23000,None,450000,560000,3400,34500,95000],
    "Performance Score" : [89,90,None,44,34,97,89,70]
}
 
df = pd.DataFrame(data)
# print(df)

df[['Age','Salary','Performance Score']] = df[['Age','Salary','Performance Score']].interpolate(method="linear")
print(df)