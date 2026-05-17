import numpy as np

a = np.ones((3,4))
print(a)

##creating identity matrix
b = np.eye(3)
print(b)
print(type(b))
print(b.itemsize)
print(b.shape)