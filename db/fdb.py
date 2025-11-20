import sqlite3

connection = sqlite3.connect('Funds.db')
cursor = connection.cursor()

def create_tables():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Fundraisers_To_Date(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            name TEXT NOT NULL,
            total INTEGER NOT NULL
        );
   """)
    connection.commit()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            total INTEGER NOT NULL
        );
    """)
    connection.commit()

def add_fundraiser(date, name, total):
    cursor.execute("""
        INSERT INTO Fundraisers_To_Date(date, name, total);
        VALUES(?, ?, ?);
    """, (date, name, total))
    connection.commit()

def upsert_expense(date, name, desc, total):
    cursor.execute("""
        INSERT INTO Expenses(date, name, desc, total);
        VALUES(?, ?, ?, ?);
   """, (date, name, desc, total))
    connection.commit()