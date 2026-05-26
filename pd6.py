import pandas as pd

df = pd.read_csv('student.csv')

print(df.head(5))
print(df.tail(6))

## Accesssing data from data frame
print(df['Name'])
print(type(df['Name']))
print(df.loc[0])
print(df.iloc[0:3])

##Accessing a specified location

print(df.at[2,'Department'])

##Accessing through iat[]

print(df.iat[2,2])