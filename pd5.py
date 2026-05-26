## creating a dataframe from a list of dictionaries
import pandas as pd
data = [
      {'Name':'Roshan','Age':45,'City':'lko'},
      {'Name':'jack','Age':45,'City':'lko'},
      {'Name':'joe','Age':45,'City':'lko'},
      {'Name':'Roshan','Age':45,'City':'lko'}
      
]

index = [1,2,3,4]

df = pd.DataFrame(data,index=index)
print(df)