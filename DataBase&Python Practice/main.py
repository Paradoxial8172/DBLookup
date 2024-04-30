import sqlite3

#opens databse (.db) file, creates one if file does not exist.
connection = sqlite3.connect("./DataBase&Python Practice/users.db") 

#creates cursor to execute commands in certain areas.
cursor = connection.cursor()

# #how to script sql commands, comment out this code when you already ran it once.
# cursor.execute("""CREATE TABLE Users (
#                firstName text,
#                lastName text,
#                phone text,
#                email text
# )""")
# #commits changes
# connection.commit()
# #closes database connection
# connection.close()

#cursor.execute("INSERT INTO Users VALUES ('Jane', 'Doe', '(121) 212-1212', 'janedoe@example.com')")

cursor.execute("SELECT * FROM Users")

print("FIRST_NAME: \t\t LAST_NAME: \t\t PHONE_NUMBER: \t\t EMAIL_ADDRESS:")
print("------------------------------------------------------------------------------------------------")
for row in cursor.fetchall():
    first_name = row[0]
    last_name = row[1]
    phone = row[2]
    email = row[3]

    print(f"{first_name} \t\t\t {last_name} \t\t\t {phone} \t {email}")
print("------------------------------------------------------------------------------------------------")

connection.close()
