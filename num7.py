import numpy as np

## Universal function (ufuncs)

##array slicing and indexing

arr = np.array([[1,2,3,4],[6,7,8,9],[10,11,12,13]])
print("Array : \n",arr)


print(arr[0][0])

print(arr[1:,2:])
print(arr[0:2])
print(arr[0:2])

print(arr[1:,1:3])

arr[0,0] = 100
print(arr)
arr[1:] = 100
print(arr)