import pandas as pd 
import numpy as np

df = pd.read_csv('Student2.csv')
print(df.head())
print(df.dtypes) 

## Handling missing values

print(df.isnull().any())
print(df.isnull().sum())
df.fillna(0, inplace = True)
print(df)