from tkinter import * # import all the classes from tkinter module for gui development.
from tkinter import messagebox # import messagebox for showing the message box.
from models.customer import Customer # import Customer class from models/cusmtomer.py

class RegisterCustomerUI: 
    """
    it is a class to handle the customer registration ui in the system.
    """
    def __init__(self, root): # it is a constructor to  initialize the customer registration ui.
        self.root = root # it stores the root window.
        self.root.title("Customer Registration") 
        self.create_register_frame() # call the create_register_frame function to create the registration frame.

    def create_register_frame(self): # it is a function to create  the registration frame.
        Label(self.root, text="Register as Customer", font=("Arial", 16)).pack(pady=10)

        Label(self.root, text="Name").pack()
        self.name_entry = Entry(self.root)
        self.name_entry.pack()

        Label(self.root, text="Address").pack()
        self.address_entry = Entry(self.root)
        self.address_entry.pack()

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

        Button( button_frame, text="Register", command=self.handle_register).pack(side=LEFT, padx=5)
        Button(button_frame, text="Go Back", command=self.go_back).pack(side=LEFT, padx=5)

    def go_back(self): # it is a function to go back to the login page.
        from .login_page import LoginPage # import LoginPage from login_page.py
        self.switch_frame(lambda: LoginPage(self.root)) # switch the frame to the login page.

    def switch_frame(self, new_frame): # it is a function to destry the widgets and calls the new frame.
        for widget in self.root.winfo_children(): # loop through all the widgets in the root window.
            widget.destroy() # destroy the widget.
        new_frame()

    def handle_register(self): # it is a function to handle the registration of the customer.
        name = self.name_entry.get() # get the name from the entry widget and store it in the name variable.
        address = self.address_entry.get() # get the address from the entry widget and store it in the address variable.
        phone_number = self.phone_entry.get() # get the phone number from the entry widget and store it in the phone_number variable.
        email = self.email_entry.get() # get the email from the entry widget and store it in the email variable.
        password = self.password_entry.get() # get the passwrd frm the entry widget and store it in the passwrd variable.
        
        if not name or not address or not phone_number or not email or not password: 
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        customer = Customer("",name, address, phone_number, email, password)
        try: # try block to catch the error if occurs.
            customer.register()
            messagebox.showinfo("Success", "Customer registered successfully!")
            self.go_back() # call the go_back function.
        except Exception as e: # catch the error if occurs.
            messagebox.showerror("Error", f"An error occurred: {e}") 