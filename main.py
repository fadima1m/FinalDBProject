import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL server host
    user="root",  # Replace with your MySQL username
    password="YU_oppdivide!20"  # Replace with your MySQL password
)

# Create a cursor object to interact with the server
cursor = connection.cursor()

# Execute the SQL query to retrieve the list of databases
cursor.execute("SHOW DATABASES")

# Fetch all the rows returned by the query
databases = cursor.fetchall()

# Print the list of databases
for database in databases:
    print(database[0])

# Close the cursor and connection
cursor.close()
connection.close()


