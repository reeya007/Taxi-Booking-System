from tkinter import * # import all tkinter module for gui development
from tkinter import messagebox # import messagebox for showing message box
from  models.admin import Admin # import Admin class from models/admin.py

def open_admin_page(root, admin): # function to openn the admin page.
    def go_back(): # function to goo back to the login page.
        from .login_page import LoginPage # import Loginpage from login_page.py
        switch_frame(lambda: LoginPage(root)) # switch the frame to the login page.

    def switch_frame(new_frame): # function to switch the frame 
        for widget in root.winfo_children(): # loop through all the widgets in the root window.
            widget.destroy() # destroy the widget.
        new_frame() # call the new_frame function.

    def assign_driver(): # function to assign the driver to the bookings.
        booking_id = booking_id_entry.get() # get the booking id from the entry widget and store it in the booking_id variable.
        driver_id = driver_id_entry.get() # get the driver id from the entry widget and store it in the driver_id variable. 
        
        if not booking_id or not driver_id: # if booking_id or driver_id is empty then show the error message.
            messagebox.showerror("Error", "Please fill in all fields.") 
            return

        try: # try block to catch the error if occurs.
            admin.assign_driver(booking_id, driver_id) 
            messagebox.showinfo("Success", "Driver assigned!") 
            switch_frame(lambda: open_admin_page(root, admin)) 
        except Exception as e: # catch the error if occurs.
            messagebox.showerror("Error", f"An error occurred: {e}") 

    root.title("Admin Dashboard") 

    bookings = admin.fetch_bookings() # fetch all the bookings which are not assigned to any driver.
    drivers = admin.fetch_drivers() # fetch all the drivers who are available for bookings.

# Main Frame
    main_frame = Frame(root)
    main_frame.pack(pady=10, padx=10)

# Bookings Section
    bookings_frame = Frame(main_frame, bd=2)
    bookings_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N)

    Label(bookings_frame, text="New Bookings", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)
    if bookings: 
     for i, booking in enumerate(bookings, start=1): # loop through all bookings.
        booking_text = f"Booking ID: {booking[0]}, Customer ID: {booking[1]}, Pickup: {booking[2]}, Dropoff: {booking[3]}, Date: {booking[4]}" 
        Label(bookings_frame, text=booking_text).grid(row=i, column=0, columnspan=2, pady=2)
    else:
     Label(bookings_frame, text="No bookings available", font=("Arial", 10)).grid(row=1, column=0, columnspan=2, pady=10)

# Vertical Line
    vertical_separator = Frame(main_frame, width=2, bd=1, relief=SUNKEN)
    vertical_separator.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky=NS)

# Drivers Section
    drivers_frame = Frame(main_frame, bd=2)
    drivers_frame.grid(row=0, column=2, padx=10, pady=10, sticky=N)

    Label(drivers_frame, text="Available Drivers", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)
    if drivers:
        for i, driver in enumerate(drivers, start=1):
            driver_text = f"Driver ID: {driver[0]}, Name: {driver[1]}, Email: {driver[2]}"
            Label(drivers_frame, text=driver_text).grid(row=i, column=0, columnspan=2, pady=2)
    else:
        Label(drivers_frame, text="No drivers available", font=("Arial", 10)).grid(row=1, column=0, columnspan=2, pady=10)

# Horizontal Line
    separator = Frame(main_frame, height=2, bd=1, relief=SUNKEN)
    separator.grid(row=1, column=0, columnspan=3, pady=10, sticky=EW)

# Assign Driver Section
    assign_frame = Frame(main_frame, bd=2)
    assign_frame.grid(row=2, column=0, padx=10, pady=10, sticky=N)

    Label(assign_frame, text="Assign Driver", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)
    Label(assign_frame, text="Booking ID").grid(row=1, column=0, padx=10, pady=5, sticky=E)
    booking_id_entry = Entry(assign_frame)
    booking_id_entry.grid(row=1, column=1, padx=10, pady=5)
    Label(assign_frame, text="Driver ID").grid(row=2, column=0, padx=10, pady=5, sticky=E)
    driver_id_entry = Entry(assign_frame)
    driver_id_entry.grid(row=2, column=1, padx=10, pady=5)
    Button(assign_frame, text="Assign Driver", command=assign_driver).grid(row=3, column=0, columnspan=2, pady=10)

# Log Out Button
    Button(main_frame, text="Log Out", command=go_back).grid(row=2, column=2, padx=10, pady=10, sticky=SE) # button to log out from the admin page

    root.mainloop() 