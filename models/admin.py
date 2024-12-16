from utils.db_connector import connect_to_db

class Admin:
     """
    It represents an Admin in the Taxi Booking System.
    
    This class provides functionalities for admin login, fetching unassigned bookings, 
    fetching available drivers, and assigning drivers to bookings.
    """
     def __init__(self, email, password):
        self.email = email # it stores admin email
        self.password = password # it stores admin password

     def login(self): # checks if admin information is valid or not
        return self.email == "admin" and self.password == "admin" # everything is right than true other wise false.

     def fetch_bookings(self): # listout all the bookings which are not assigned to any driver.
        conn = connect_to_db() 
        cursor = conn.cursor()
        query = "SELECT * FROM Bookings WHERE driver_id IS NULL" # query to fetch all the bookings which are not assigned to any driver.
        cursor.execute(query)
        bookings = cursor.fetchall()
        conn.close()
        return bookings # return all the bookings which are not assigned to any driver.

     def fetch_drivers(self): 
        """ Fetch all the drivers who are available for bookings 
        and lists of drivers who are available for bookings.
        """
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "SELECT id, name, email FROM Drivers where is_available = 1"
        cursor.execute(query)
        drivers = cursor.fetchall()
        conn.close()
        return drivers

     def assign_driver(self, booking_id, driver_id):
        """ Assign a driver to a booking and update their availability. 
        """
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "UPDATE Bookings SET driver_id = %s WHERE id = %s" 
        driver_query = "UPDATE Drivers SET is_available = 0 WHERE id = %s" 
        try: # try block to catch the error if occurs.
            cursor.execute(query, (driver_id, booking_id))
            cursor.execute(driver_query, (driver_id,))
            conn.commit()
        except Exception as e: # catch the erroe if occurs.
            raise e # raise the error.
        finally: 
            conn.close()