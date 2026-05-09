import pandas as pd

# df = pd.read_csv(r"C:\Users\sures\Downloads\sales_data_sample.csv", encoding ="latin1")
# df = pd.read_excel(r"C:\Users\sures\Downloads\SampleSuperstore.xlsx",engine = "openpyxl")
df = pd.read_json(r"C:\Users\sures\Downloads\sample_Data.json")

print(df)