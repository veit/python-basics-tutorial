import sqlite3

# create books database
conn = sqlite3.connect("library.db")

cursor = conn.cursor()

# create books table
cursor.execute("""CREATE TABLE books
                  (title text, language text, author text, license text,
                          release_date text)
               """)
