from tkinter import *
from tkinter import messagebox
from models.customer import Customer # import Customer class from models/customer.py

def open_customer_page(root, customer_id, name): 
    """
    function to open the customer dashboard where customer can book and view their bookings.
    """
    customer = Customer(customer_id) # create a customer object with the given customer_id.

    def go_back(): # function to go back to the login page.
        from .login_page import LoginPage # import LoginPage from login_page.py
        switch_frame(lambda: LoginPage(root)) # switch the frame to the login page.

    def switch_frame(new_frame):
        """
        function to destroy the widgets and call the new frames.
        """
        for widget in root.winfo_children(): # loop through all the widget in the root window.
            widget.destroy() # destroy tge widget.
        new_frame() # call the new_frame function.

    def book_trip(): 
        """
        function to book a trip for the customer by taking the input such as pickup location dropoff location date time.
        """
        pickup = pickup_entry.get() # get the pickup location from the entry widget and store it in the pickup variable.
        dropoff = dropoff_entry.get() 
        trip_date = trip_date_entry.get()
        
        if not pickup or not dropoff or not trip_date: # if pickup or dropoff or trip_date is empty then show the erroe message.
            messagebox.showerror("Error", "Please fill in all fields.") 
            return

        try: # try block to catch the error if occurs.
            customer.book_trip(pickup, dropoff, trip_date) #
            messagebox.showinfo("Success", "Booking successful!")
            switch_frame(lambda: open_customer_page(root, customer_id, name))
        except Exception as e: # catch the error if occurs.
            messagebox.showerror("Error", f"An error occurred: {e}")

    def cancel_booking(): # function to cancel the booking of the customer by providing the booking id.
        booking_id = booking_id_entry.get() # get the booking id from the entry widget and store it in the booking_id variable.
        
        if not booking_id: # if booking_id is empty then show the error message.
            messagebox.showerror("Error", "Please enter a booking ID.") 
            return

        try: # try block to catch the error if occurs.
            customer.cancel_booking(booking_id) # cancel the booking of the customer.
            messagebox.showinfo("Success", "Booking cancelled!")
            switch_frame(lambda: open_customer_page(root, customer_id, name))
        except Exception as e: # catch the error if occurs.
            messagebox.showerror("Error", f"An error occurred: {e}") 

    root.title("Customer Dashboard") 
    welcome_text = f"Welcome, {name}"

    Label(root, text=welcome_text, font=("Arial", 16)).pack(pady=10)

# Main Frame
    main_frame = Frame(root)
    main_frame.pack(pady=10, padx=10)

# Booking Section
    booking_frame = Frame(main_frame, bd=2)
    booking_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N)

    Label(booking_frame, text="Book a Taxi", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)
    Label(booking_frame, text="Pickup Location").grid(row=1, column=0, padx=10, pady=5, sticky=E)
    pickup_entry = Entry(booking_frame)
    pickup_entry.grid(row=1, column=1, padx=10, pady=5)
    Label(booking_frame, text="Dropoff Location").grid(row=2, column=0, padx=10, pady=5, sticky=E)
    dropoff_entry = Entry(booking_frame)
    dropoff_entry.grid(row=2, column=1, padx=10, pady=5)
    Label(booking_frame, text="Trip Date (YYYY-MM-DD HH:MM)").grid(row=3, column=0, padx=10, pady=5, sticky=E)
    trip_date_entry = Entry(booking_frame)
    trip_date_entry.grid(row=3, column=1, padx=10, pady=5)
    Button(booking_frame, text="Book Trip", command=book_trip).grid(row=4, columnspan=2, pady=10)

    # Vertical Line
    vertical_separator = Frame(main_frame, width=2, bd=1, relief=SUNKEN)
    vertical_separator.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky=NS)

    # Bookings Section
    bookings_frame = Frame(main_frame, bd=2)
    bookings_frame.grid(row=0, column=2, padx=10, pady=10, sticky=N)

    Label(bookings_frame, text="My Bookings", font=("Arial", 16)).pack(pady=10)

    bookings = customer.fetch_bookings("current")
    completed_bookings = customer.fetch_bookings("completed")

    if bookings: 
        for booking in bookings: # loop through all the bookings
            booking_text = f"Booking ID: {booking[0]}, Pickup: {booking[2]}, Dropoff: {booking[3]}, Date: {booking[4]}"
            Label(bookings_frame, text=booking_text).pack(pady=2)
    else:
         Label(bookings_frame, text="You don't have any bookings yet", font=("Arial", 10)).pack(pady=10) 

# Horizontal Line
    separator = Frame(main_frame, height=2, bd=1, relief=SUNKEN)
    separator.grid(row=1, column=0, columnspan=3, pady=10, sticky=EW)

# Cancel Booking Section
    cancel_frame = Frame(main_frame, bd=2)
    cancel_frame.grid(row=2, column=0, padx=10, pady=10, sticky=N)

    Label(cancel_frame, text="Cancel Booking", font=("Arial", 16)).grid(row=0, columnspan=2, pady=10)
    Label(cancel_frame, text="Booking ID").grid(row=1, column=0, padx=10, pady=5, sticky=E)
    booking_id_entry = Entry(cancel_frame)
    booking_id_entry.grid(row=1, column=1, padx=10, pady=5)
    Button(cancel_frame, text="Cancel Booking", command=cancel_booking).grid(row=2, columnspan=2, pady=10)

# Completed booking section
    completed_frame = Frame(main_frame, bd=2)
    completed_frame.grid(row=2, column=2, padx=10, pady=10, sticky=N)

    Label(completed_frame, text="Completed Bookings", font=("Arial", 16)).pack(pady=10)

    if completed_bookings:
        for booking in completed_bookings:
            booking_text = f"Booking ID: {booking[0]}, Pickup: {booking[2]}, Dropoff: {booking[3]}, Date: {booking[4]}"
            Label(completed_frame, text=booking_text).pack(pady=2)
    else:
        Label(completed_frame, text="You don't have any completed bookings yet", font=("Arial", 10)).pack(pady=10)

# Log Out Button
    Button(main_frame, text="Log Out", command=go_back).grid(row=3, column=2, columnspan=2 ,padx=10, pady=10, sticky=SE) # button to log out from the customer page.
    root.mainloop()