import csv
import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Read the csv file
with open("../books.csv", encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=",")
    # Insert records from into the database
    cursor.executemany("INSERT INTO books VALUES (?,?,?,?,?)", reader)

# Save data to database
conn.commit()
