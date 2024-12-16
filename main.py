from tkinter import * #import tkinter for the gui development.
from views.login_page import LoginPage # import LoginPage from login_page.py

class App: 
    """
    it is a class to handle the app.
    """
    # Constructor for the App class
    def __init__(self):
        self.root = Tk() 

    # Function to run the app
    def run(self):
        self.root.configure(bg="lightblue")
        self.root.option_add("*Background", "lightblue")
        self.root.option_add("*Entry.Background", "white")
        LoginPage(self.root)
        self.root.mainloop()

# Entry point of the application
if __name__ == "__main__":
    app = App() # Create an instance of the App class
    app.run() # Run the app