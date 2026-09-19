import seaborn as sns
import matplotlib.pyplot as plt

#categorical plots
##bar plots
tips = sns.load_dataset('tips')
sns.barplot(x = 'day',y = 'total_bill',data = tips)
plt.title('bar plot of total bill by day')
plt.show()

