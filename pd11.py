import pandas as pd

df = pd.read_csv('missing.csv')

## fetching the first 5 rows 
print(df.head(5))
print(df.dtypes)


# Handling missing values

print()

print(df.isnull)

df.fillna(0, inplace = True) # filling the missing values with 0
print(df)

# filling the missing values with the mean of the column

df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print(df)