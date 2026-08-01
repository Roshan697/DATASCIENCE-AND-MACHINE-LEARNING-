import pandas as pd

data = {
    "Name":["Roshan","Rahul","Priya","Amit","Neha"],
    "Age":[21,22,20,23,21],
    "Marks":[85,90,88,76,95],
    "City":["Lucknow","Delhi","Mumbai","Jaipur","Pune"]
    
}

df = pd.DataFrame(data)

df.to_excel("student6.xlsx",index = False)
print("Excel file saved successfully!")