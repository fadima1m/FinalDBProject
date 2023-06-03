import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL server host
    user="root",  # Replace with your MySQL username
    password="YU_oppdivide!20"  # Replace with your MySQL password
)

# Create a cursor object to interact with the server
cursor = connection.cursor()

# Execute the SQL query to create the database
cursor.execute("CREATE DATABASE menagerie")

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()