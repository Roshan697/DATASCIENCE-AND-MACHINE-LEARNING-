import seaborn as sns 
import matplotlib.pyplot as plt

#heat map 

tips = sns.load_dataset('tips')

corr = tips[['total_bill','tip','size']].corr()

sns.heatmap(corr,annot = True,cmap = 'coolwarm')
plt.show()
print(corr)