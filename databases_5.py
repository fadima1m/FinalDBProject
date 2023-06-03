import mysql.connector

# Connect to the MySQL server
connection = mysql.connector.connect(
    host="localhost",  # Replace with your MySQL server host
    user="root",  # Replace with your MySQL username
    password="YU_oppdivide!20",  # Replace with your MySQL password
    database="menagerie"  # Replace with the name of your database
)

# Create a cursor object to interact with the server
cursor = connection.cursor()

# Execute the SQL query to select all records from the "pet" table
cursor.execute("SELECT * FROM pet")

# Fetch all the rows returned by the query
records = cursor.fetchall()

# Print the column headers
column_names = [desc[0] for desc in cursor.description]
print("\t".join(column_names))

# Print the records
for record in records:
    print("\t".join(str(value) for value in record))

# Close the cursor and connection
cursor.close()
connection.close()
