import matplotlib.pyplot as plt
import numpy as np

##Multiple plots
##sample data

x = [1,2,3,4,5]
y1 = [10,20,15,25,30]
y2 = [100,200,150,250,300]

plt.figure(figsize=(10,5))
plt.subplot(1,2,1)
plt.plot(x,y1,color ='green')
plt.title('plot 1')
plt.show()