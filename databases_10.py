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

# Execute the SQL query to count pets for each owner
query = "SELECT owner, COUNT(*) AS pet_count FROM pet GROUP BY owner"
cursor.execute(query)

# Fetch all the rows returned by the query
records = cursor.fetchall()

# Print the column headers
print("Owner\t\tPet Count")

# Print the records
for record in records:
    owner, pet_count = record
    print(f"{owner}\t\t{pet_count}")

# Close the cursor and connection
cursor.close()
connection.close()
