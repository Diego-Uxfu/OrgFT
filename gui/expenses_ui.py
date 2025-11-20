import tkinter as tk
from tkinter import ttk

from db.fdb import *


class ExpensesWindow(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        header = tk.Label(self, text="Expenses", bg="white")
        header.pack(pady=5)

                            ### ------------ user input buttons -------------- ###
                              #Current Has: Desc, amount, date, name, reimburse#

        # frame containing inputs
        input_frame = tk.Frame(self, bg="white")
        input_frame.pack(pady=5, padx=5, fill="x")

        # description
        tk.Label(input_frame, text="Description:", bg="white").grid(row=0, column=0, sticky="w", pady=5)
        self.desc_entry = tk.Entry(input_frame, width=30)
        self.desc_entry.grid(row=0, column=1, pady=5, padx=5)

        # amount input box
        tk.Label(input_frame, text="Amount: $", bg="white").grid(row=1, column=0, sticky="w", pady=5)
        self.amount_entry = tk.Entry(input_frame, width=30)
        self.amount_entry.grid(row=1, column=1, pady=5, padx=5)

        # date input
        tk.Label(input_frame, text="Date:", bg="white").grid(row=2, column=0, sticky="w", pady=5)
        self.date_entry = tk.Entry(input_frame, width=30)
        self.date_entry.grid(row=2, column=1, pady=5, padx=5)

        # name of person who made expense
        tk.Label(input_frame, text="Name:", bg="white").grid(row=3, column=0, sticky="w", pady=5)
        self.name_entry = tk.Entry(input_frame, width=30)
        self.name_entry.grid(row=3, column=1, pady=5, padx=5)

        #reimbursement status
        tk.Label(input_frame, text="Reimbursed?", bg="white").grid(row=4, column=0, sticky="w", pady=5)
        self.reimburse_var = tk.StringVar()
        self.reimburse_dropdown = ttk.Combobox(input_frame, textvariable=self.reimburse_var,
                                              values=["Yes", "No", "Partial"], width=28, state="readonly")
        self.reimburse_dropdown.grid(row=2, column=1, pady=5, padx=5)

                    ### ----------------- action buttons -------------------- ###
        # holds the buttons
        button_frame = tk.Frame(self, bg="white")
        button_frame.pack(pady=10)

        # confirms the addition of the expense
        add_button = tk.Button(
            button_frame, text="Add Expense", command=self.add_expense, bg="green", fg="white",padx=10)
        add_button.pack(side="left", padx=5)

        # return button
        back_button = tk.Button(
            button_frame, text="Back", command=lambda: controller.show_frame("MainPage"), bg="gray",fg="white", padx=10)
        back_button.pack(side="left", padx=5)


                    ### ----------------- Display -------------------- ###
        # Expenses List Frame
        list_frame = tk.Frame(self, bg="white")
        list_frame.pack(pady=10, padx=10, fill="both", expand=True)

        tk.Label(list_frame, text="Recent Expenses:", bg="white", font=("Arial", 12, "bold")).pack(anchor="w")

        # Treeview for displaying expenses
        self.tree = ttk.Treeview(list_frame, columns=("Date", "Description", "Amount", "Category"), height=10)
        self.tree.column("#0", width=0, stretch="no")
        self.tree.column("Date", width=100, anchor="w")
        self.tree.column("Description", width=150, anchor="w")
        self.tree.column("Amount", width=80, anchor="e")
        self.tree.column("Category", width=100, anchor="w")

        self.tree.heading("#0", text="", anchor="w")
        self.tree.heading("Date", text="Date", anchor="w")
        self.tree.heading("Description", text="Description", anchor="w")
        self.tree.heading("Amount", text="Amount", anchor="e")
        self.tree.heading("Category", text="Category", anchor="w")

        self.tree.pack(fill="both", expand=True)

        # Load expenses on initialization
        self.load_expenses()

        def add_expense(self):
            date = self.date_entry.get()
            name = self.name_entry.get()
            description = self.desc_entry.get()
            amount = float(self.amount_entry.get())

            upsert_expense(date, name, description, amount)