import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sai_@1234",
    database="training_db"
)

cursor = conn.cursor()

cursor.execute("INSERT INTO students VALUES (1, 'Rahul', 21)")
cursor.execute("INSERT INTO students VALUES (2, 'Priya', 22)")

conn.commit()

print("Data inserted")

conn.close()