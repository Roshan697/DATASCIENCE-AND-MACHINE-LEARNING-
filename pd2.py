import pandas as pd

##creating a series form dictionary

data = {'a':1,'b':2,'c':3}

series_dict = pd.Series(data)
print(series_dict)
