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

# Execute the SQL query to select the name and birth columns from the "pet" table
query = "SELECT name, birth FROM pet"
cursor.execute(query)

# Fetch all the rows returned by the query
records = cursor.fetchall()

# Print the column headers
print("Name\t\tBirth")

# Print the records
for record in records:
    name, birth = record
    print(f"{name}\t\t{birth}")

# Close the cursor and connection
cursor.close()
connection.close()
