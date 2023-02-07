import psycopg2

conn = psycopg2.connect(dbname="my_db", user="username")
cursor = conn.cursor()

# Execute a query
cursor.execute("SELECT * FROM my_table")
row = cursor.fetchone()

# Close your cursor and connection
cursor.close()
conn.close()
