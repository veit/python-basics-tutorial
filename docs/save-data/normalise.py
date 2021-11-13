import sqlite3

conn = sqlite3.connect("library.db")
cursor = conn.cursor()

cursor.execute("""CREATE TABLE languages
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  language_code VARCHAR(2))"""
               )

cursor.execute("""INSERT INTO languages (language_code)
                  VALUES ('de')"""
               )

cursor.execute("""INSERT INTO languages (language_code)
                  VALUES ('en')"""
               )

cursor.execute("""CREATE TABLE "temp" (
                  "id" INTEGER,
                  "title" TEXT,
                  "language_code" INTEGER REFERENCES languages(id),
                  "language" TEXT,
                  "author" TEXT,
                  "license" TEXT,
                  "release_date" DATE,
                  PRIMARY KEY("id" AUTOINCREMENT)
                  )"""
               )

cursor.execute("""INSERT INTO temp (title,language,author,license,release_date)
                  SELECT title,language,author,license,release_date FROM books"""
               )

cursor.execute("""UPDATE temp
                  SET language_code = 1
                  WHERE language = 'de'"""
               )

cursor.execute("""UPDATE temp
                  SET language_code = 2
                  WHERE language = 'en'"""
               )

# Only SQLite ≥ 3.35.0 allows DROP COLUMN;
# Only Python versions ≥ 3.8 released after 27 April 2021 will receive these or
# newer SQLite versions.
cursor.execute("""ALTER TABLE temp DROP COLUMN language"""
               )

cursor.execute("""DROP TABLE books"""
               )

cursor.execute("""ALTER TABLE temp RENAME TO books"""
               )

conn.commit()
