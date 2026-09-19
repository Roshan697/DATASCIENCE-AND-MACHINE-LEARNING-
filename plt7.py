import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y1 = [10,20,15,25,30]
y2 = [5,15,10,20,25]

plt.figure(figsize=(10,5))

#first plot
plt.subplot(2,2,1)
plt.plot(x,y1,color = 'green')
plt.title('plot 1')

#second plot
plt.subplot(2,2,2)
plt.plot(y1,x,color = 'blue')
plt.title ('plot 2')

plt.subplot(2,2,3)
plt.plot(x,y2,color = 'red')
plt.title("plot 3")



plt.subplot(2,2,4)
plt.plot(x,y2,color = 'green')
plt.title("plot 4")

plt.show()
