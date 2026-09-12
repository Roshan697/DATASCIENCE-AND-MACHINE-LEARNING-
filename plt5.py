import matplotlib.pyplot as plt

#sample data
x1 = [1,2,3,4,5]
x2 = [1,3,4,5,6]
y1 = [10,20,15,25,30]
y2 = [100,200,150,250,300] 
x3 = [1,2,3,4,5]
y3=[10,20,15,25,30]
plt.subplot(3,2,1)
plt.plot(x1,y1,color ='green')
plt.subplot(1,2,2)
plt.plot(x2,y2,color ='blue')

plt.subplot(2,2,3)
plt.plot(x3,y3,color ='red')
plt.show()