import os
import sqlite3
import unittest

import create_db


class TestCreateDB(unittest.TestCase):
    def test_db_exists(self):
        assert os.path.exists("library.db")

    def test_table_exists(self):
        with self.assertRaises(sqlite3.OperationalError):
            create_db.cursor.execute("CREATE TABLE books(title text)")


class TestCommands(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        cursor = self.conn.cursor()

        cursor.execute(
            """CREATE TABLE books
                          (title text, language text, author text, license text,
                                  release_date text)
                       """
        )

        cursor.execute(
            """INSERT INTO books
                          VALUES ('Python basics', 'en', 'Veit Schiele', 'BSD',
                                  '2021-10-28')"""
        )

    def test_func_like(self):
        self.conn = sqlite3.connect(":memory:")
        cursor = self.conn.cursor()
        sql = "SELECT * FROM books WHERE title LIKE Python"
        cursor.execute(sql, "")


# In order to use the file as a script as well as an importable module, the code
# that parses the command line only runs if the module is executed as the “main”
# file.
if __name__ == "__main__":
    unittest.main()
