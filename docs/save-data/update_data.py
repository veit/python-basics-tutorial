import sqlite3


def update_license(old_name, new_name):
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()
    sql = f"""
    UPDATE books
    SET license = '{new_name}'
    WHERE license = '{old_name}'
    """
    cursor.execute(sql)
    conn.commit()

if __name__ == '__main__':
    update_license(old_name='BSD',
                  new_name='BSD-3-Clause')
