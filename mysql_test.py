import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sai_@1234",
    database="training_db"
)

print("Connected Successfully!")

conn.close()