import matplotlib.pyplot as plt
import numpy as np

labels = ['A','B','C','D','E']

sizes = [30,20,49,23,12]

colors = ['gold','yellowgreen', 'lightcoral','lightskyblue','purple']

explode = (0.09,0,0,0,0)

#creating a pipechart 

plt.pie(sizes,labels = labels,colors = colors,explode = explode,autopct="%1.1f%%",shadow = True)
plt.show()