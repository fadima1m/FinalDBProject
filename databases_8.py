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

# Execute the SQL query to select record(s) of female dogs from the "pet" table
query = "SELECT * FROM pet WHERE species = 'dog' AND (sex = 'f' OR sex IS NULL)"
cursor.execute(query)

# Fetch all the rows returned by the query
records = cursor.fetchall()

# Print the number of records returned
print("Number of Records:", len(records))

# Print the column headers
column_names = [desc[0] for desc in cursor.description]
print("\t".join(column_names))

# Print the records
for record in records:
    print("\t".join(str(value) if value else "" for value in record))

# Close the cursor and connection
cursor.close()
connection.close()
