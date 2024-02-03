import mysql.connector
import pandas as pd

# Read the Excel file, skipping the first row which contains headers
df = pd.read_excel("data/Public-List-of-Accreditation_8.xlsx", skiprows=1)

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
database_name = "AccommodationsDB"
create_database_query = f"CREATE DATABASE IF NOT EXISTS {database_name}"

cursor = connection.cursor()
cursor.execute(create_database_query)

print(f"Database '{database_name}' created successfully")

# Switch to the new database
cursor.execute(f"USE {database_name}")

# Create a table with the required fields
create_table_query = """
CREATE TABLE IF NOT EXISTS Accommodation (
    Accreditation_Number VARCHAR(255),
    Number_of_Beds INT,
    Email VARCHAR(255),
    Cell_Number VARCHAR(20),
    Street_Address VARCHAR(255),
    Nearest_Campus VARCHAR(255),
    Residence_Name VARCHAR(255)
)
"""

cursor.execute(create_table_query)
print("Table 'Accommodation' created successfully")

# Insert data into the table
for _, row in df.iterrows():
    insert_query = """
    INSERT INTO Accommodation (Accreditation_Number, Number_of_Beds, Email, Cell_Number, Street_Address, Nearest_Campus, Residence_Name)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    record = tuple(row)
    cursor.execute(insert_query, record)

print("Data inserted successfully")

# Commit the changes
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
