from utils.db_connector import connect_to_db 

class Customer:
    """it  defines the Customer class which represents a customer in the taxi booking system.
    """
    def __init__(self, customer_id, name=None, address=None, phone=None, email=None, password=None): # it is constructor to initialize customer object with the given attributes.
        self.customer_id = customer_id # it stores the customer id.
        self.name = name # it stores the customer name.
        self.address = address # it stores the customer address.
        self.phone = phone # it stores the customer phone number.
        self.email = email # it stores the customer email.
        self.password = password # it stores the customer password.

    def register(self): # it is a funtion to register the  new customer in the system. 
        conn = connect_to_db() 
        cursor = conn.cursor() #
        query = """
        INSERT INTO Customers (name, address, phone_number, email, password)
        VALUES (%s, %s, %s, %s, %s)
        """
        try: # try block to catch the error if occurs.
            cursor.execute(query, (self.name, self.address, self.phone, self.email, self.password)) 
            conn.commit()
        except Exception as e:
            raise e # raise the error if occurs.
        finally:
            conn.close()

    # it is a function to fetch the bookings of the customer based on the type current and completed.
    def fetch_bookings(self, type): 
        conn = connect_to_db()
        cursor = conn.cursor()
        if type == "current":
            query = "SELECT * FROM Bookings WHERE customer_id = %s AND is_completed = 0"
        elif type == "completed":
            query = "SELECT * FROM Bookings WHERE customer_id = %s AND is_completed = 1"
        cursor.execute(query, (self.customer_id,))
        bookings = cursor.fetchall() # fetch all the bookinngs of the customer.
        conn.close()
        return bookings

    def book_trip(self, pickup, dropoff, trip_date): # it is a function to book a trip for the customer.
        conn = connect_to_db()
        cursor = conn.cursor()
        query = "INSERT INTO Bookings (customer_id, pickup_location, dropoff_location, trip_date) VALUES (%s, %s, %s, %s)"
        try: #try block to catch the error if occurs.
            cursor.execute(query, (self.customer_id, pickup, dropoff, trip_date))
            conn.commit()
        except Exception as e: # catch the error if occurs.
            raise e # raise the error.
        finally: # finally block to close the connection.
            conn.close()

    def cancel_booking(self, booking_id): # it is a function to cancel the booking of the customer.
        conn = connect_to_db()
        cursor = conn.cursor()
        booking_query = "SELECT * FROM Bookings WHERE id = %s"
        cursor.execute(booking_query, (booking_id,))
        booking = cursor.fetchone() # fetch the booking of the customer.

        if booking[6]:
            raise Exception("Booking already completed!")

        if not booking:  # if booking is not found then raise the exception.
            raise Exception("Booking not found!") 
        driver_id = booking[5] # get the driver id from the booking. 
        
        query = "DELETE FROM Bookings WHERE id = %s" # query to delete the booking.
        driver_query = "UPDATE Drivers SET is_available = 1 WHERE id = %s"
        try:
            cursor.execute(query, (booking_id,)) 
            if driver_id:
                cursor.execute(driver_query, (driver_id,))
            conn.commit()
        except Exception as e:
            raise e 
        finally:
            conn.close()
            

        
    
