import matplotlib as plt 
##Multiple plots

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y1 = [1,3,5,6,7]
y2= [12,3,4,53,3]

plt.figure(figsize=(9,5))


plt.subplot(1,2,1)
plt.plot(x,y1,color = 'green')
plt.title("Plot 1")
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.show()


