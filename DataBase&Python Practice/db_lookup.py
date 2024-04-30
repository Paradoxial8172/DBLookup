import sqlite3
from user import NewUser
from tkinter import *
from tkinter import messagebox

root = Tk()
root.resizable(height=False, width=False)

title = Label(root, text="Database Lookup", font=("Arial", 16, "bold"))
or_label = Label(root, text="Or...", font=("Arial", 12, "bold"))
label_one = Label(root, text="Enter first name:")
label_two = Label(root, text="Enter last name:")
label_three = Label(root, text="Enter email:")
entry_one = Entry(root)
entry_two = Entry(root)
entry_three = Entry(root)

first_name_label = Label(root, text="First Name: N/A")
last_name_label = Label(root, text="Last Name: N/A")
email_label = Label(root, text="Email: N/A")
phone_label = Label(root, text="Phone Number: N/A")

title.pack(padx=80, pady=10)
label_one.pack(padx=80, pady=10)
entry_one.pack(padx=80, pady=10)
label_two.pack(padx=80, pady=10)
entry_two.pack(padx=80, pady=10)
or_label.pack(padx=80, pady=10)
label_three.pack(padx=80, pady=10)
entry_three.pack(padx=80, pady=10)

first_name_label.pack(padx=80)
last_name_label.pack(padx=80)
email_label.pack(padx=80)
phone_label.pack(padx=80)

def lookup():
    
    connection = sqlite3.connect("./DataBase&Python Practice/users.db") 
    cursor = connection.cursor()

    if entry_one.get() and entry_two.get():
        first_name = entry_one.get().lower()
        last_name = entry_two.get().lower()
        query = "SELECT * FROM Users WHERE LOWER(firstName)=? AND LOWER(lastName)=?"
        cursor.execute(query, (first_name, last_name))
        row = cursor.fetchone()
        if row:
            firstname, lastname, phone, email = row
            first_name_label.configure(text=f"First Name: {firstname}")
            last_name_label.configure(text=f"Last Name: {lastname}")
            email_label.configure(text=f"Email: {email}")
            phone_label.configure(text=f"Phone Number: {phone}")
        else:
            first_name_label.configure(text="User not found")
            last_name_label.configure(text="")
            email_label.configure(text="")
            phone_label.configure(text="")
    elif entry_three.get():
        email_address = entry_three.get()
        query = f"SELECT * FROM Users WHERE LOWER(email)='{email_address}'"
        cursor.execute(query)
        row = cursor.fetchone()
        if row:
            firstname, lastname, phone, email = row
            first_name_label.configure(text=f"First Name: {firstname}")
            last_name_label.configure(text=f"Last Name: {lastname}")
            email_label.configure(text=f"Email: {email}")
            phone_label.configure(text=f"Phone Number: {phone}")
        else:
            first_name_label.configure(text="User not found")
            last_name_label.configure(text="")
            email_label.configure(text="")
            phone_label.configure(text="")
    else:
        first_name_label.configure(text="User not found")
        last_name_label.configure(text="")
        email_label.configure(text="")
        phone_label.configure(text="")

    connection.close()

def add_user():
    top_lvl = Toplevel(root)
    l1 = Label(top_lvl, text="Enter First Name:")
    l2 = Label(top_lvl, text="Enter Last Name:")
    l3 = Label(top_lvl, text="Enter Email:")
    l4 = Label(top_lvl, text="Enter Phone:")
    first_name_entry = Entry(top_lvl)
    last_name_entry = Entry(top_lvl)
    email_entry = Entry(top_lvl)
    phone_entry = Entry(top_lvl)

    l1.pack(padx=80, pady=10)
    first_name_entry.pack(padx=80, pady=10)
    l2.pack(padx=80, pady=10)
    last_name_entry.pack(padx=80, pady=10)
    l3.pack(padx=80, pady=10)
    email_entry.pack(padx=80, pady=10)
    l4.pack(padx=80, pady=10)
    phone_entry.pack(padx=80, pady=10)

    def save_and_exit():
        try:
            # Establish connection and create cursor
            connection = sqlite3.connect("./DataBase&Python Practice/users.db")
            cursor = connection.cursor()

            # Create a new user object
            new_user = NewUser(first_name_entry.get(), last_name_entry.get(), email_entry.get(), phone_entry.get())

            # Insert the new user into the database
            query = "INSERT INTO Users VALUES (?, ?, ?, ?)"
            cursor.execute(query, new_user.get_values())

            # Commit the transaction to persist changes
            connection.commit()
        except sqlite3.Error as e:
            # Handle any errors and roll back the transaction
            print("Error adding user:", e)
            messagebox.showinfo("Error.", f"Error adding user: {e}. Try deleting users.db-journal?")
            connection.rollback()
        finally:
            # Close the connection and destroy the top-level window
            connection.close()
            top_lvl.destroy()
            messagebox.showinfo("Success!", "User has been added to the database!")

    save_btn = Button(top_lvl, text="Save & Exit", command=save_and_exit)
    save_btn.pack(padx=80, pady=10)

    top_lvl.grab_set()
    top_lvl.mainloop()

lookup_btn = Button(root, text="Look Up", command=lookup)    
lookup_btn.pack( padx=80, pady=10)
add_user_btn = Button(root, text="Add User", command=add_user)
add_user_btn.pack( padx=80, pady=10)

root.mainloop()
