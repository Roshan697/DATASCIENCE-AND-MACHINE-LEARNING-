import pandas as pd

## Data aggregating and grouping

df = pd.read_csv('missing.csv')
#print(df.head())

grouped_mean = df.groupby('Name')['Age'].mean()
print(df)

grouped_sum = df.groupby(['Department','Marks'])['Salary'].sum()
print(grouped_sum)

group_by = df.groupby('Name')['Age']
print(group_by)

## Aggregate multiple function 
groupe_agg = df.groupby('Name')['Age'].agg(['mean','sum','count'])
print(groupe_agg)