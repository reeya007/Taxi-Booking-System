from tkinter import * # import tkinter for the gui development.
from tkinter import messagebox # import messagebox for showing the message box.
from models.driver import Driver # import driver class from models/driver.py

class RegisterDriverUI: 
    """
    it is a class to handle the driver registration ui in the system.
    """
    def __init__(self, root): # it is a constructor to initialize the driver registration ui.
        self.root = root 
        self.root.title("Driver Registration")
        self.create_register_frame()

    def create_register_frame(self):# it is a function to create the registration frame.
        Label(self.root, text="Register as Driver", font=("Arial", 16)).pack(pady=10)

        Label(self.root, text="Name").pack()
        self.name_entry = Entry(self.root)
        self.name_entry.pack()

        Label(self.root, text="License Number").pack()
        self.license_entry = Entry(self.root)
        self.license_entry.pack()

        Label(self.root, text="Phone").pack()
        self.phone_entry = Entry(self.root)
        self.phone_entry.pack()

        Label(self.root, text="Email").pack()
        self.email_entry = Entry(self.root)
        self.email_entry.pack()

        Label(self.root, text="Password").pack()
        self.password_entry = Entry(self.root, show="*")
        self.password_entry.pack()

        button_frame = Frame(self.root)
        button_frame.pack(pady=10)

        Button(button_frame, text="Register", command=self.handle_register).pack(side=LEFT, padx=5)
        Button(button_frame, text="Go Back", command=self.go_back).pack(side=LEFT, padx=5)

    def go_back(self): # it is a function to go back to the login page.
        from .login_page import LoginPage # import LoginPage from login_page.py
        self.switch_frame(lambda: LoginPage(self.root)) # switch the frame to the login page.

    def switch_frame(self, new_frame): # it is a function to destry the widgets and calls the new frame.
        for widget in self.root.winfo_children(): # loop through all the widget in the root window.
            widget.destroy() # destroy the widget.
        new_frame()

    def handle_register(self): # it is a function to handle the registration of the driver.
        name = self.name_entry.get() # get the name from the entry widget and store it in the name variable.
        license_number = self.license_entry.get() # get the license number from the entry widget and store it in the license_number variable.
        phone_number = self.phone_entry.get() # get the phone number from the entry widget and store it in the phone_number variable.
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        if not name or not license_number or not phone_number or not email or not password: # if the name or license_number or phone_number or email or passwrd is empty then show the error message.
            messagebox.showerror("Error", "Please fill in all fields.") 
            return

        driver = Driver("", name, license_number, phone_number, email, password)
        try: # try block to catch the error if occurs.
            driver.register()
            messagebox.showinfo("Success", "Driver registered successfully!")
            self.go_back() # call the go_back function.
        except Exception as e: # catch the error if occurs.
            messagebox.showerror("Error", f"An error occurred: {e}")