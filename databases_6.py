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

# Define the data to be inserted into the "pet" table
data = [
    ("Fluffy", "Harold", "cat", "f", "1993-02-04", None),
    ("Claws", "Gwen", "cat", "m", "1994-03-17", None),
    ("Buffy", "Harold", "dog", "f", "1989-05-13", None),
    ("Fang", "Benny", "dog", "m", "1990-08-27", None),
    ("Bowser", "Diane", "dog", "m", "1979-08-31", "1995-07-29"),
    ("Chirpy", "Gwen", "bird", "f", "1998-09-11", None),
    ("Whistler", "Gwen", "bird", None, "1997-12-09", None),
    ("Slim", "Benny", "snake", "m", "1996-04-29", None)
]

# Execute the SQL query to insert the data into the "pet" table
insert_query = "INSERT INTO pet (name, owner, species, sex, birth, death) VALUES (%s, %s, %s, %s, %s, %s)"
cursor.executemany(insert_query, data)

# Commit the changes to the database
connection.commit()

# Close the cursor and connection
cursor.close()
connection.close()
