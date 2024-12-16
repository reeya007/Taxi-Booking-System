import mysql.connector

# Function to connect to the database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql.reeya",
        database="TaxiBooking"
    )

