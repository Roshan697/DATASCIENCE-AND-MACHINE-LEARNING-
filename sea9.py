import seaborn as sns 
import matplotlib.pyplot as plt

import pandas as pd

sales_df = pd.read_csv('student4.csv')
print(sales_df.head())

## plot total sales by product

plt.figure(figsize=(10,6))

sns.barplot(x='Name', y = 'Marks',data = sales_df,estimator = sum)
plt.show()