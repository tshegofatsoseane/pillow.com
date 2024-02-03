import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="98Naturena!!"
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL server")

# Create a new database
database_name = "newdatabase"
create_database_query = f"CREATE DATABASE {database_name}"

cursor = connection.cursor()
cursor.execute(create_database_query)

print(f"Database '{database_name}' created successfully")

# Close the cursor and connection
cursor.close()
connection.close()
