'''filling the missing values with
the mean of the column'''

import pandas as pd

df = pd.read_csv('Student2.csv')

print(df.isnull().any())
print(df.isnull().sum())
df['Marks_fillna'] = df['Marks'].fillna(df['Marks'].mean())
print(df)

##accessing at specified element
print(df['Name'])
print(df.at[1,'Student_ID']) 