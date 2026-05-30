'''Data Manipulation with DB'''
import pandas as pd

df = pd.read_csv('Student2.csv')

#Adding a column
df['Pension'] = [50000,60000,70000,90000,100000,42839,34820,38191,58349,43802]
print(df)

df.drop