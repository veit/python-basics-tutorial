import sqlite3

def delete_by_language(language):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    sql = f"""
    DELETE FROM books
    WHERE language = '{language}'
    """
    cursor.execute(sql)
    conn.commit()

delete_by_language(language='de')
