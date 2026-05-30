import pandas as pd

df = pd.read_csv('missing.csv')
print(df)

df['Marks'] = df['Marks'].fillna(df['Marks'].mean())
print(df)

print(df.dtypes)

##Renaming columns

df.rename(columns={'Department': 'course'}, inplace=True)
print(df.head())

## changing the datatypes
df['Age_new'] = df['Age'].fillna(df['Age'].mean()).astype(float)
print(df.head())

df['New Value'] = df['Age'].apply(lambda x:x*2)
print(df)

