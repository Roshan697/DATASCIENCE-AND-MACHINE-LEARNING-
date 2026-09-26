import sqlite3


## connect to an sqlite database 

connection = sqlite3.connect('Roshan.db')
print(connection)

cursor = connection.cursor()

# create a table

cursor.execute('''
               
Create Table If Not Exists employees(
    id Integer Primary Key,
    name Text Not Null,
    Age Integer,
    Department text
)
               ''')

## Insert the data in sqlite3 table

cursor.execute('''Insert into employees(name, Age, Department)
               values('Roshan',22,'Data Scientist')
               ''')
 
 
cursor.execute('''Insert into employees(name, Age, Department)
               values('Bob',22,'SDE2')
               ''')

cursor.execute('''Insert into employees(name, Age, Department)
               values('Charlie',22,'Finance')
               ''')
## Commit the changes 

connection.commit()

## Query the data from the sqlite from the table itself
cursor.execute('Select *from employees')
rows = cursor.fetchall()

##print the queried data



## update the data in the table
cursor.execute('''
UPDATE employees
set age = 34
where name = 'Roshan'
               ''')

connection.commit()

## Fetch the updated data




#delete the data from the table
cursor.execute('''
               delete from employees 
               where name = 'Bob'
               ''')

cursor.execute('SELECT *from employees')
rows = cursor.fetchall()


for row in rows:
    print(row)
