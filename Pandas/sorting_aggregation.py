## SORTING
# sorting data in 1 coloumn 

import pandas as pd

data ={
    "Name": ['Bharat','Raut','Suresh'],
    "Age" :   [10,6,57],
    "Salary" : [10000,3000,2000]
}

df= pd.DataFrame(data)
df.sort_values(by = "Age" , ascending= True , inplace= True   )
print('sorted age by descending')
print(df)