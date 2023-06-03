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

# Execute the SQL query to create the "pet" table
cursor.execute("""
    CREATE TABLE pet (
        name VARCHAR(20),
        owner VARCHAR(20),
        species VARCHAR(20),
        sex CHAR(1),
        birth DATE,
        death DATE
    )
""")

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
