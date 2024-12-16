from utils.db_connector import connect_to_db

class Driver: 
    """ it defines the driver class which represents a driver in the taxi booking system.This class contains functions to register a driver and fetch their assigned trips.
    """
    def __init__(self, driver_id, name = None, license_number = None, phone = None, email = None, password = None): # it is a constructor to initialize the driver object with the given attributes.
        self.driver_id = driver_id 
        self.name = name
        self.license_number = license_number
        self.phone = phone
        self.email = email
        self.password = password

    def register(self): # it is a function to register the new driver in the system.
        conn = connect_to_db()
        cursor = conn.cursor()
        query = """
        INSERT INTO Drivers (name, license_number, phone_number, email, password)
        VALUES (%s, %s, %s, %s, %s)
        """
        try: # try block to catch the error if occurs.
            cursor.execute(query, (self.name, self.license_number, self.phone, self.email, self.password))
            conn.commit()
        except Exception as e: # catch the error if occurs.
            raise e # raise the error.
        finally: 
            conn.close()
    
    # it is a function to fetch the trips assigned to the drivers based on the type current and completed.
    def fetch_assigned_trips(self, type): 
        conn = connect_to_db()
        cursor = conn.cursor()

        if type == "current":
            query = "SELECT * FROM Bookings WHERE driver_id = %s AND is_completed = 0"
        elif type == "completed":
            query = "SELECT * FROM Bookings WHERE driver_id = %s AND is_completed = 1"

        cursor.execute(query, (self.driver_id,))
        trips = cursor.fetchall()
        conn.close()
        return trips
    
    # Function to mark the assigned trip as completed.
    def complete_trip(self, booking_id): 
        if not booking_id: # if the booking_id is empty then return.
            return
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "UPDATE Bookings SET is_completed = 1 WHERE id = %s AND driver_id = %s"
        driver_query = "UPDATE Drivers SET is_available = 1 WHERE id = %s"
        try: # try block to catch the error if occurs.
            cursor.execute(query, (booking_id, self.driver_id))
            cursor.execute(driver_query, (self.driver_id,))
            conn.commit()
        except Exception as e: 
            raise e 
        finally: 
            conn.close()