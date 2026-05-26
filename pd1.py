import pandas as pd

## Series
'''panda series is a 1D array like object which 
can hold any data type. It is similar to a column
in a table. '''

data = [1,2,3,4,5]
series = pd.Series(data)
print("Series \n",series)