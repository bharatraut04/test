import pandas as pd

## ROWS ##

# df = pd.read_csv(r"C:\Users\sures\Downloads\sales_data_sample.csv", encoding ="latin1")
# df = pd.read_excel(r"C:\Users\sures\Downloads\SampleSuperstore.xlsx",engine = "openpyxl")
# df = pd.read_json(r"C:\Users\sures\Downloads\sample_Data.json")

# print("display first 10 rows")
# print(df.head())

# print("display last 10 rows")
# print(df.tail())

## UNDERSTANDING THE DATA ##

# df = pd.read_json(r"C:\Users\sures\Downloads\sample_Data.json")
# print("display the info of dataset")
# print(df.info())

## DESCRIBE METHOD ##

# data = {
#     "Name" : ['bharat','suresh','raut','sangita','gunjan','joe','raj','ram'],
#     "Age" : [21,34,56,23,23,25,28,31],
#     "Salary" : [50000,23000,120000,450000,560000,3400,34500,95000],
#     "Perforamnce Score" : [89,90,65,44,34,97,89,70]
# }

# df = pd.DataFrame(data)
# print("sample dataframe")
# print(df)
# print("descriptive statistics")
# print(df.info())
# print(df.describe()) 

## SHAPE AND COLUMN ##

# data = {
#     "Name" : ['bharat','suresh','raut','sangita','gunjan','joe','raj','ram'],
#     "Age" : [21,34,56,23,23,25,28,31],
#     "Salary" : [50000,23000,120000,450000,560000,3400,34500,95000],
#     "Perforamnce Score" : [89,90,65,44,34,97,89,70]
# }

# df = pd.DataFrame(data)
# print(df)
# print(f'shape:{df.shape}')
# print(f'column Name:{df.columns}')



## MODIFICATION IN SELECTED COLUMNS ##

# data = {
#     "Name" : ['bharat','suresh','raut','sangita','gunjan','joe','raj','ram'],
#     "Age" : [21,34,56,23,23,25,28,31],
#     "Salary" : [50000,23000,120000,450000,560000,3400,34500,95000],
#     "Perforamnce Score" : [89,90,65,44,34,97,89,70]
# }

# df = pd.DataFrame(data)
# print("Sample DataFrame")
# print(df)
# print("Name(single column return series)")
# print(df["Name"])
# #selecting multiple columns
# subset = df[["Name","Salary"]]
# print('\nsubset with name & salary')
# print(subset)



## MODIFICATION IN SELECTED ROWS ##

data = {
    "Name" : ['bharat','suresh','raut','sangita','gunjan','joe','raj','ram'],
    "Age" : [21,34,56,23,23,25,28,31],
    "Salary" : [50000,23000,120000,450000,560000,3400,34500,95000],
    "Perforamnce Score" : [89,90,65,44,34,97,89,70]
}

df = pd.DataFrame(data)

high_salary = df[df["Salary"]>50000]
print(high_salary)

print("\nHigh Salary & High Age")
high_salary1 = df[(df["Salary"]>50000) & (df["Age"]>30)]
print(high_salary1)

#using OR condition 
print("\nOR condition")
filtered_or = df[(df["Age"]>25) | (df["Perforamnce Score"]>90)]
print(filtered_or)
