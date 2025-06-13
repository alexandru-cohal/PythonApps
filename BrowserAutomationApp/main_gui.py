import tkinter as tk
from tkinter import messagebox
from main import WebAutomation


class App:
    def __init__(self, root_window):
        """ Set the GUI """

        self.root = root_window
        self.root.title("Browser Automation App")

        # Login frame
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=10, pady=10)

        tk.Label(self.login_frame, text="Username").grid(row=0, column=0, sticky="w")
        self.entry_username = (tk.Entry(self.login_frame))
        self.entry_username.grid(row=0, column=1, sticky="ew")
        tk.Label(self.login_frame, text="Password").grid(row=1, column=0, sticky="w")
        self.entry_password = tk.Entry(self.login_frame, show="*")
        self.entry_password.grid(row=1, column=1, sticky="ew")

        # Form submission frame
        self.form_frame = tk.Frame(self.root)
        self.form_frame.pack(padx=10, pady=10)

        tk.Label(self.form_frame, text="Full Name").grid(row=0, column=0, sticky="w")
        self.entry_full_name = tk.Entry(self.form_frame)
        self.entry_full_name.grid(row=0, column=1, sticky="ew")
        tk.Label(self.form_frame, text="Email").grid(row=1, column=0, sticky="w")
        self.entry_email = tk.Entry(self.form_frame)
        self.entry_email.grid(row=1, column=1, sticky="ew")
        tk.Label(self.form_frame, text="Current Address").grid(row=2, column=0, sticky="w")
        self.entry_current_address = tk.Entry(self.form_frame)
        self.entry_current_address.grid(row=2, column=1, sticky="ew")
        tk.Label(self.form_frame, text="Permanent Address").grid(row=3, column=0, sticky="w")
        self.entry_permanent_address = tk.Entry(self.form_frame)
        self.entry_permanent_address.grid(row=3, column=1, sticky="ew")

        # Buttons frame
        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(padx=10, pady=10)

        tk.Button(self.buttons_frame, text="Submit", command=self.submit_data).grid(row=0, column=0, padx=5)
        tk.Button(self.buttons_frame, text="Close Browser", command=self.close_browser).grid(row=0, column=1, padx=5)

    def submit_data(self):
        """ Open the webpage in the browser, login, fill in the form and submit it """

        # Get the introduced information
        username = self.entry_username.get()
        password = self.entry_password.get()
        full_name = self.entry_full_name.get()
        email = self.entry_email.get()
        current_address = self.entry_current_address.get()
        permanent_address = self.entry_permanent_address.get()

        # Open the webpage, login, fill in the form and submit it
        self.web_automation = WebAutomation()
        self.web_automation.login(username=username,
                                  password=password)
        self.web_automation.fill_form(full_name=full_name,
                                      email=email,
                                      current_address=current_address,
                                      permanent_address=permanent_address)

    def close_browser(self):
        """ Close the browser """

        self.web_automation.close()
        messagebox.showinfo(title="Done",
                            message="Browser closed!")


root_window = tk.Tk()
app = App(root_window)
root_window.mainloop()