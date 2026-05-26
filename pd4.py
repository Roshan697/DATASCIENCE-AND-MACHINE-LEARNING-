import pandas as pd
##Dataframe

##create a dataframe from a dictionary of list

data = {
    'Name':['krish','john','jack'],
    'Age':[25,30,45],
    'City':['banglore','NY','lko']
    
}

df = pd.DataFrame(data)
print(df)
print(type(df))