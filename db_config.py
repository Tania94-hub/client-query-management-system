import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="client_query_db"
)

cursor = connection.cursor()

print("MySQL Connected Successfully")