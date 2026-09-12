import pandas as pd

#reading from html tables

url = "https://www.w3schools.com/html/html_tables.asp"
tables = pd.read_html(url)

print("Number of tables",len(tables))
print(tables[0])
