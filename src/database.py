import sqlite3
conn = sqlite3.connect("")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL
)
""")

cursor.execute("INSERT INTO Users VALUES ('Ohms', 'password')")

conn.commit()

cursor.execute("SELECT * FROM Users")
rows = cursor.fetchall()

for row in rows:
    print(row)