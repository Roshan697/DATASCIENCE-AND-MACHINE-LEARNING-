import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [1,3,5,6,7]

## create a customized line plot

print(plt.plot(x,y))
plt.plot(x,y,color='purple', linestyle = '-.',marker = 'o',linewidth = 3,markersize = 4)
plt.grid(True)

plt.show()