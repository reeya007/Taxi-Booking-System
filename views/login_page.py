from tkinter import * 
from tkinter import messagebox 
from .customer_page import open_customer_page 
from .driver_page import open_driver_page 
from .admin_page import open_admin_page 
from .customer_register import RegisterCustomerUI 
from .driver_register import RegisterDriverUI
from utils.db_connector import connect_to_db
from models.admin import Admin

class LoginPage: 
    """
     it is a class to handle the login page in the system.
    """
    def __init__(self, root): 
        """
        it is a constructor to initialize the login page.
        """
        self.root = root 
        self.root.title("Taxi Booking System - Login") 
        # self.root.geometry("800x800")
        self.role_var = StringVar(value="Customer")
        self.email_var = StringVar(value="")
        self.password_var = StringVar(value="")
        self.create_login_frame() 

    def create_login_frame(self): 
        """
          it is a function to create the login frame.
          """
        Label(self.root, text="Welcome to Taxi booking System", font=("Arial", 16)).pack(pady=10) 
        Label(self.root, text="Please select your role and login or register:" ).pack()

        role_frame = Frame(self.root,  )
        role_frame.pack(pady=5)
        Radiobutton(role_frame, text="Customer",  variable=self.role_var, value="Customer").pack(side=LEFT, padx=5)
        Radiobutton(role_frame, text="Driver",  variable=self.role_var, value="Driver").pack(side=LEFT, padx=5)
        Radiobutton(role_frame, text="Admin",  variable=self.role_var, value="Admin").pack(side=LEFT, padx=5)

        Label(self.root,  text="Email").pack()
        Entry(self.root, textvariable=self.email_var).pack()
        Label(self.root, text="Password").pack()
        Entry(self.root, textvariable=self.password_var, show="*").pack()

        button_frame = Frame(self.root, background='lightblue')
        button_frame.pack(pady=10)
        Button(button_frame, text="Login", command=self.handle_login).pack(side=LEFT, padx=5)
        Button(button_frame, text="Register", command=self.handle_register).pack(side=LEFT, padx=5)

    def switch_frame(self, new_frame): 
        """
          it is a function to destroy the widgets and calls the new frame.
          """
        for widget in self.root.winfo_children(): # loop through all the widgets in the root window.
            widget.destroy() # destroy the widget.
        new_frame()

    def handle_login(self): 
        """
        it is a function to handle the login of the user.
        """
        role = self.role_var.get() # get the role from the role variable and store it in the role variable.
        email = self.email_var.get() # get the email from the email variable and store it in the email variable.
        password = self.password_var.get()
        
        if not email or not password: # if the email or password is empty then slow the error message.
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        conn = connect_to_db()
        cursor = conn.cursor()
        if role == "Customer": 
            query = "SELECT * FROM Customers WHERE email = %s AND password = %s"
        elif role == "Driver":
            query = "SELECT * FROM Drivers WHERE email = %s AND password = %s"
        elif role == "Admin":
            admin = Admin(email, password)
            if admin.login():
                self.switch_frame(lambda: open_admin_page(self.root, admin))
                return
            else:
                messagebox.showerror("Error", "Invalid admin credentials!")
                return
        cursor.execute(query, (email, password))
        result = cursor.fetchone()
        conn.close()
        if result:
            user_id = result[0]
            name = result[1]
            if role == "Customer":
                self.switch_frame(lambda: open_customer_page(self.root, user_id, name))
            elif role == "Driver":
                self.switch_frame(lambda: open_driver_page(self.root, user_id, name))
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def handle_register(self): 
        """
          it is  the function to handle the registration of the user.
          """
        role = self.role_var.get() # get the role from the role variable and store it in the role variable.
        if role == "Customer": # if the role is customer then switch the frame to the RegisterCustomerUI.
            self.switch_frame(lambda: RegisterCustomerUI(self.root)) # switch the frame to the RegisterCustomerUI.
        elif role == "Driver": # if the role is driver then switch the frame to the RegisterDriverUI.
            self.switch_frame(lambda: RegisterDriverUI(self.root)) # switch the frame to the registerdriverui.
        else:# if the role is admin then show the info message.
            messagebox.showinfo("Info", "Admins cannot register from here!") 