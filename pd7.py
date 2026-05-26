import pandas as pd

## Data manipulation dataframes

df = pd.read_csv('Student.csv')

df['salary'] = [50000,60000,70000,48239,43820,71938,48292,43285,68590,13253]

df.drop('Marks',axis = 1, inplace=True)


# Add age to the columns

df['Age'] = df['Age']+1

print(df.iloc[0:4])

df.drop(0,inplace=True)
print(df)
print(df.describe())

