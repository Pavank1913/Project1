import sqlite3

# Connect to the database
conn = sqlite3.connect('contacts.db')
cursor = conn.cursor()

# Create a table to store contacts if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS contacts
              (ID INTEGER PRIMARY KEY AUTOINCREMENT,
               Name TEXT,
               Cell TEXT,
               Email TEXT)''')

# Insert 5 rows of data
contacts_data = [
    ('John Doe', '1234567890', 'john.doe@example.com'),
    ('Jane Smith', '9876543210', 'jane.smith@example.com'),
    ('Alice Johnson', '5555555555', 'alice.johnson@example.com'),
    ('Bob Brown', '9999999999', 'bob.brown@example.com'),
    ('Charlie Davis', '8888888888', 'charlie.davis@example.com')
]

cursor.executemany('INSERT INTO contacts (Name, Cell, Email) VALUES (?, ?, ?)', contacts_data)
conn.commit()

# Fetch all the data and display it
cursor.execute('SELECT * FROM contacts')
all_contacts = cursor.fetchall()

for contact in all_contacts:
    print(f'ID: {contact[0]}, Name: {contact[1]}, Cell: {contact[2]}, Email: {contact[3]}')

# Close the connection
conn.close()
