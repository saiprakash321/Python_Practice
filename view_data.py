import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sai_@1234",
    database="training_db"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

conn.close()