import matplotlib.pyplot as plt
import numpy as np

##bar plot

categories = ['A','B','C','D','E']
values = [5,7,3,8,6]

#create a bar plot
plt.bar(categories,values,color='maroon')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar plot')
plt.show()

