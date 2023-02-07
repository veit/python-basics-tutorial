import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# insert a record into the database
cursor.execute(
    """INSERT INTO books
                  VALUES ('Python basics', 'en', 'Veit Schiele', 'BSD',
                          '2021-10-28')"""
)

# save data to database
conn.commit()

# insert multiple records using the more secure "?" method
new_books = [
    ("Jupyter Tutorial", "en", "Veit Schiele", "BSD-3-Clause", "2019-06-27"),
    ("Jupyter Tutorial", "de", "Veit Schiele", "BSD-3-Clause", "2020-10-26"),
    ("PyViz Tutorial", "en", "Veit Schiele", "BSD-3-Clause", "2020-04-13"),
]
cursor.executemany("INSERT INTO books VALUES (?,?,?,?,?)", new_books)
conn.commit()
