## Normalisation concepts -- Normalization
## to have a mean of 0 and standatd deviation of 1
import numpy as np

##calculating the mean and the standard deviation
data = np.array([1,2,3,4,5])

mean = np.mean(data)
std_dev = np.std(data)
normalized_data = (data - mean)/ std_dev
print (normalized_data)



