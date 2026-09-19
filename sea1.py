import seaborn as sns
import matplotlib.pyplot as plt

#basic plotting with seaborn
tips = sns.load_dataset('tips')
print(tips)

#create a scatter plot

sns.scatterplot(x = 'total_bill', y = 'tip',data = tips)

plt.title("scatter plot of total bill vs tips")

plt.show()

