import pandas as pd
from io import StringIO

Data = '{"employee_name":"James", "email":"james@gmail.com","job_profile":[{"title1":"Team Lead","title2":"Sr. Developer"}]}'
df = pd.read_json(StringIO(Data))
print(df)

read = df.to_json()
print(read)

read2 = df.to_json(orient = 'index') 
print(read2)

read3 = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
print(read3)

read4 = df.to_csv("wine.csv")