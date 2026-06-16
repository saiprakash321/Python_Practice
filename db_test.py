import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sai_@1234",
    database="training_db"
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
)
""")

print("Table ready")

conn.close()