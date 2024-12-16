from tkinter import * # import tkinter for the gui development.
from tkinter import messagebox # import messagebox for showing the message box.
from models.driver import Driver # import Driver class from models/driver.py

def open_driver_page(root, driver_id, name): 
    """
    it is a function to open the driver dashboard where driver can view their assigned trips.
    """
    driver = Driver(driver_id) # create a driver object with the given driver_id.

    def go_back(): 
        """
        it is a function to go back to the login page.
        """
        from .login_page import LoginPage # import LoginPage from login_page.py
        switch_frame(lambda: LoginPage(root)) # switch the frame to the login page.

    def switch_frame(new_frame): 
        """
          it is a function to destry the widgets and calls the new frame.
         """
        for widget in root.winfo_children(): # loop through all the widgets in the root window.
            widget.destroy() # destroy the widget.
        new_frame()

    def complete_trip(booking_id):
        if not booking_id:
            messagebox.showerror("Error", "Please enter a booking ID.")
            return
        driver.complete_trip(booking_id)
        messagebox.showinfo("Success", "Trip marked as completed!")
        switch_frame(lambda: open_driver_page(root, driver_id, name))

    root.title("Driver Dashboard") 

    current_trip = driver.fetch_assigned_trips("current") # fetch the current trip assigned to the driver.
    completed_trip = driver.fetch_assigned_trips("completed") # fetch the completed trip assigned to the driver.

    # Welcome section 
    welcome_text = f"Welcome, {name}"
    Label(root, text=welcome_text, font=("Arial", 16)).pack(pady=10)

    # Main Frame
    main_frame = Frame(root)
    main_frame.pack(pady=10, padx=10)

    # Ongoing Trips Section
    ongoing_frame = Frame(main_frame, bd=2)
    ongoing_frame.grid(row=0, column=0, padx=10, pady=10, sticky=N)

    Label(ongoing_frame, text="My Ongoing Trip", font=("Arial", 14)).pack(pady=10)

    if current_trip: # if the trips are available then show the trips.
        for trip in current_trip: # loop through all the trips.
            trip_text = f"Booking ID: {trip[0]}, Pickup: {trip[2]}, Dropoff: {trip[3]}, Date: {trip[4]}"
            Label(ongoing_frame, text=trip_text).pack(pady=2)
    else:
        Label(ongoing_frame, text="No ongoing trip", font=("Arial", 10)).pack(pady=10)
    
    # Vertical Line
    vertical_separator = Frame(main_frame, width=2, bd=1, relief=SUNKEN)
    vertical_separator.grid(row=0, column=1, rowspan=3, padx=10, pady=10, sticky=NS)

    # Completed Trips Section
    completed_frame = Frame(main_frame, bd=2)
    completed_frame.grid(row=0, column=2, padx=10, pady=10, sticky=N)

    Label(completed_frame, text="My Completed Trips", font=("Arial", 14)).pack(pady=10)

    if completed_trip:
        for trip in completed_trip:
            trip_text = f"Booking ID: {trip[0]}, Pickup: {trip[2]}, Dropoff: {trip[3]}, Date: {trip[4]}"
            Label(completed_frame, text=trip_text).pack(pady=2)
    else:
        Label(completed_frame, text="No completed trip", font=("Arial", 10)).pack(pady=10)

    # Horizontal Line
    separator = Frame(main_frame, height=2, bd=1, relief=SUNKEN)
    separator.grid(row=1, column=0, columnspan=3, pady=10, sticky=EW)

    # Mark Trip as Completed Section
    mark_frame = Frame(main_frame, bd=2)
    mark_frame.grid(row=2, column=0, padx=10, pady=10, sticky=N)

    Label(mark_frame, text="Mark Trip as Completed", font=("Arial", 14)).grid(row=0, column=0, columnspan=2, pady=10)
    Label(mark_frame, text="Booking ID").grid(row=1, column=0, padx=10, pady=5, sticky=E)
    booking_id_entry = Entry(mark_frame)
    booking_id_entry.grid(row=1, column=1, padx=10, pady=5)
    Button(mark_frame, text="Mark as Completed", command=lambda: complete_trip(booking_id_entry.get())).grid(row=2, column=0, columnspan=2, pady=10)

    # Log Out Button
    Button(main_frame, text="Log Out", command=go_back).grid(row=2, column=2, columnspan=2, padx=10, pady=10, sticky=SE) # button to log out from the driver page.
    root.mainloop()