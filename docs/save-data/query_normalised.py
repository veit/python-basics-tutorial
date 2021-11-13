import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

def select_all_records_ordered_by_language_number(cursor):
    print("All books ordered by language id and title:")
    for row in cursor.execute("""SELECT language_code, author, title FROM books
                                 ORDER BY language_code,title"""):
        print(row)

def select_all_records_ordered_by_language_code(cursor):
    print("All books ordered by language code and title:")
    for row in cursor.execute("""SELECT languages.language_code, books.author, books.title
                                 FROM books
                                 JOIN languages ON (books.language_code = languages.id)
                                 ORDER BY languages.language_code,title"""):
        print(row)

select_all_records_ordered_by_language_number(cursor)
select_all_records_ordered_by_language_code(cursor)
