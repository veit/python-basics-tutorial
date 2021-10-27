import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

def select_all_records_from_author(cursor, author):
    print(f"All books from {author}:")
    sql = "SELECT * FROM books WHERE author=?"
    cursor.execute(sql, [author])
    print(cursor.fetchall())  # or use fetchone()

def select_all_records_sorted_by_author(cursor):
    print("Listing of all books sorted by author:")
    for row in cursor.execute("SELECT rowid, * FROM books ORDER BY author"):
        print(row)

def select_using_like(cursor, text):
    print(f"All books with {text} in the title:")
    sql = f"""
    SELECT * FROM books
    WHERE title LIKE '{text}%'"""
    cursor.execute(sql)
    print(cursor.fetchall())

select_all_records_from_author(cursor, author='Veit Schiele')
select_all_records_sorted_by_author(cursor)
select_using_like(cursor, text='Python')
