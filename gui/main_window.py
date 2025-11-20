import sqlite3
import tkinter as tk
from db.actions import *

class MainPage(tk.Tk):
    def __init__(self, conn):
        super().__init__()
        self.connection = conn #connection into database to avoid global vars; makes accessible in all

        self.title("Track sheet")
        self.geometry("700x500")

        # Create a Frame (the container)
        container = tk.Frame(self, bg="white", padx=5, pady=5)
        container.pack(fill="both", expand=True, padx=5, pady=5)

        # Add widgets *inside* the container
        label = tk.Label(container, text="Track sheet", bg="lightblue")
        label.pack(pady=5)

        view_button = tk.Button(container, text="View Expenses", command=view_expenses)
        view_button.pack(pady=5)

        reimburse_button = tk.Button(container, text="Reimburse Expenses", command=view_reimburse)
        reimburse_button.pack(pady=5)

        funds_button = tk.Button(container, text="View Funds", command=view_Funds)
        funds_button.pack(pady=5)

if __name__ == "__main__":
    import sqlite3
    connection = sqlite3.connect("db.sqlite")

    app = MainPage(connection)
    app.mainloop()

