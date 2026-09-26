import sqlite3

connection = sqlite3.connect('sales_data.db')
cursor = connection.cursor()

cursor.execute(
    '''
    Create table if not exists sales(
        id INTEGER PRIMARY KEY,
        date TEXT NOT NULL,
        product TEXT NOT NULL,
        sales INTEGER,
        region TEXT
    )
    '''
)

sales_data = [
    ('2023-01-01','Product1',100,'North'),
    ('2023-01-02','Product2',200, 'South'),
    ('2023-01-03','Product1',150,'East'),
    ('2023-01-04','Product3',300,'West')
]

connection.commit()


cursor.executemany('''
             Insert into sales(date,product,sales,region)
             values(?,?,?,?)      
                   ''',sales_data)

connection.commit()

cursor.execute('SELECT * FROM sales')
rows = cursor.fetchall()

for row in rows:
    print(row)
    
##close the connection

connection.close()