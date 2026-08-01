import sqlite3

# Create or open database
conn = sqlite3.connect("college.db")

# Create cursor
cursor = conn.cursor()

# Drop old table (optional for practice)
cursor.execute("DROP TABLE IF EXISTS STUDENTS")

# Create table
cursor.execute("""
CREATE TABLE STUDENTS(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    marks INTEGER
)
""")

# Insert data
cursor.execute("INSERT INTO STUDENTS VALUES (1, 'Roshan', 21, 85)")
cursor.execute("INSERT INTO STUDENTS VALUES (2, 'Rahul', 22, 90)")

# Save
conn.commit()

# Close
conn.close()

print("Database created successfully!")